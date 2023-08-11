"""Слово"""


def main():
    word = input()
    up, down = 0, 0
    for w in word:
        if w.islower():
            down += 1
        else:
            up += 1
    print(word.upper()) if up > down else print(word.lower())


if __name__ == "__main__":
    main()