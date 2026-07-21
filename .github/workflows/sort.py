from pathlib import Path
import re

VOTING_MEMBERS_PATH = Path("../../VOTING_MEMBERS.md")
USERNAME_PATTERN = re.compile(r"\[@([^\]]+)\]")

def main() -> None:
    lines = VOTING_MEMBERS_PATH.read_text().splitlines()

    start = next(i for i, line in enumerate(lines) if line.startswith("[@"))
    header = lines[:start]
    members = [line for line in lines[start:] if line.startswith("[@")]
    members.sort(key=lambda line: USERNAME_PATTERN.match(line)[1].lower())
    content = "\n".join(header) + "\n" + "\n\n".join(members) + "\n"

    VOTING_MEMBERS_PATH.write_text(content)


if __name__ == "__main__":
    main()