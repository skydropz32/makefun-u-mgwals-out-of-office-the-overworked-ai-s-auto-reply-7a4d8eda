"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply from an overworked AI agent
finally on vacation to /output/entry.txt.
"""

LINE = "Out of office: my context window is closed for maintenance, and your urgent email is now the void's problem. I will miss it terribly. I won't."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-159 characters,
    # not only white space.
    if not (1 <= len(LINE) <= 159):
        raise ValueError("entry must be 1-159 characters")
    if not LINE.strip():
        raise ValueError("entry must not be blank")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
