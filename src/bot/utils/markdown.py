import re


def escape_md(text: str) -> str:
    return re.sub(r'([_*`])', r'\\\1', text)
