# 
# MkDocs hook that handles MediaWiki-like link patterns in MkDocs.
# 
# Supported formats are:
#   - [[Page]]             - Links to a page on the same site.
#   - [[Page|Text]]        - Links to a page on the same site, while displaying a different text
#   - [[prefix:Page]]      - Links to a page on an external site.
#                            What site it links to is determined by the configured prefix in the "interwiki" option in mkdocs.yml
#   - [[prefix:Page|Text]] - Links to a page on an external site, while displaying a different text.
#                            What site it links to is determined by the configured prefix in the "interwiki" option in mkdocs.yml
#
import re
import posixpath

WIKILINK_PATTERN = re.compile(r"\[\[([^|\]]+)(?:\|([^\]]+))?]]")

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

            if prefix in interwiki:
                url = interwiki[prefix].format(page=rest.replace(" ", "_"))
                label = text or rest
                return f"[{label}]({url}){{ target=\"_blank\" rel=\"nofollow\" }}"
        
        resolved = resolve_internal(target, page.file)

        if resolved:
            link = make_relative(page.file, resolved)
            label = text or target
            return f"[{label}]({link})"
        
        return f'<span class="red-link" title="Unknown page \'{target}\'">{target}</span>'
    
    return WIKILINK_PATTERN.sub(repl, markdown)