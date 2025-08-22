import re
from typing import Optional


def find_score(text: str) -> Optional[int]:
    result = re.search(r"Оцінка:\s*(\d)/\d", text)
    return int(result.group(1)) if result else result
