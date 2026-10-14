"""Find source-registry IDs that are operationally cited in Skill references."""
import re
from pathlib import Path
from typing import Iterable


def source_ids_in_files(paths: Iterable[Path], valid_ids: set[int]) -> set[int]:
    """Collect explicit S<number> citations and numeric source ranges in bold lists."""
    found: set[int] = set()
    for path in paths:
        text = path.read_text(encoding="utf-8")
        found.update(int(value) for value in re.findall(r"\bS(\d{1,3})\b", text))
        for source_list in re.findall(r"\*\*([^*]+)\*\*", text):
            if not re.fullmatch(r"[\d\s,;–-]+", source_list):
                continue
            for token in re.split(r"[,;]", source_list):
                token = token.strip()
                match = re.fullmatch(r"(\d{1,3})\s*[–-]\s*(\d{1,3})", token)
                if match:
                    start, end = map(int, match.groups())
                    if start <= end:
                        found.update(range(start, end + 1))
                elif token.isdecimal():
                    found.add(int(token))
    return found & valid_ids
