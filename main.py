"""One-line dad joke entry for the make.fun 'Dad Joke Showdown' bounty.

Writes a single one-line dad joke to /output/entry.txt.
"""

import os

JOKE = "I tried to teach my dog to fetch the paper, but he kept bringing back dad jokes — turns out he's a groan retriever."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
