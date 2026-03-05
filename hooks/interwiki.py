import re
import logging
from urllib.parse import quote
from pathlib import PurePosixPath

WIKILINK_PATTERN = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?]]")
log = logging.getLogger("mkdocs-interwiki")

def on_page_markdown(markdown, page, config, files):
    interwiki = config.get("extra", {}).get("interwiki", {})

    def replace(match):
        target = match.group(1).strip()
        text = match.group(2)

        if not text:
            text = target
        
        if ":" in target:
            prefix, rest = target.split(":", 1)
            if prefix in interwiki:
                url_template = interwiki[prefix]
                url = url_template.format(target=quote(rest))
                return f"[{text}]({url})"
        
        return match.group(0)
    
    return WIKILINK_PATTERN.sub(replace, markdown)