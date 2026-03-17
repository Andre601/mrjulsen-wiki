# 
# ProperDocs hook that handles MediaWiki-like link patterns in ProperDocs.
# 
# Supported formats are:
#   - [[Page]]             - Links to a page on the same site.
#   - [[Page|Text]]        - Links to a page on the same site, while displaying a different text
#   - [[prefix:Page]]      - Links to a page on an external site.
#                            What site it links to is determined by the configured prefix in the "interwiki" option in properdocs.yml
#   - [[prefix:Page|Text]] - Links to a page on an external site, while displaying a different text.
#                            What site it links to is determined by the configured prefix in the "interwiki" option in properdocs.yml
#
import re
import posixpath
import logging
from collections import defaultdict
from pathlib import Path
from properdocs.plugins import get_plugin_logger

WIKILINK_PATTERN = re.compile(r"\[\[([^|\]]+)(?:\|([^\]]+))?]]")

log = get_plugin_logger(__name__)

pages_map = {}
interwiki = {}

def on_config(config):
    global interwiki
    interwiki = config.get("extra", {}).get("interwiki", {})

    return config

def on_files(files, config):
    global pages_map

    pages_map = {}

    for f in files:
        if f.src_uri.endswith(".md"):
            name = f.src_uri.rsplit("/", 1)[-1].replace(".md", "")
            pages_map.setdefault(name.lower(), []).append(f)
    
    return files

def resolve_internal(name, current_file):
    candidates = pages_map.get(name.lower().replace(" ", "_"))
    if not candidates:
        return None
    
    current_dir = posixpath.dirname(current_file.src_uri)

    def distance(f):
        target_dir = posixpath.dirname(f.src_uri)
        rel = posixpath.relpath(target_dir, current_dir)
        return rel.count("../")
    
    return sorted(candidates, key=distance)[0]

def make_relative(current_file, target_file):
    src_dir = posixpath.dirname(current_file.src_uri)
    target = target_file.src_uri
    return posixpath.relpath(target, src_dir)


def on_page_markdown(markdown, page, config, files):
    def repl(match):
        target = match.group(1).strip()
        text = match.group(2)
        
        if ":" in target:
            prefix, rest = target.split(":", 1)
            label = text or rest

            if prefix in interwiki:
                url = interwiki[prefix].format(page=rest.replace(" ", "_"))
                return f'[{label}]({url}){{ target="_blank" rel="nofollow" }}'
            else:
                log.warning(f'Unknown Interwiki prefix "{prefix}" in "{page.file.src_uri}"!')
                return f'<span class="red-link" title="Unknown Interwiki prefix \'{prefix}\'">{text}</span>'
        
        resolved = resolve_internal(target, page.file)

        label = text or target

        if resolved:
            link = make_relative(page.file, resolved)
            return f'[{label}]({link})'
        
        log.warning(f'Unknown target page "{target}" in "{page.file.src_uri}"!')
        return f'<span class="red-link" title="Unknown target page \'{target}\'">{label}</span>'
    
    if page.meta and page.meta.get("no_wikilinks", False):
        log.info(f"Skipping ignored page {page.file.src_uri}")
        return markdown
    
    return WIKILINK_PATTERN.sub(repl, markdown)