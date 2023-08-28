"""Быстрый математик"""


def main():
    first = input()
    second = input()
    print("".join(["0" if first[i] == second[i] else "1" for i in range(len(first))]))


if __name__ == "__main__":
    main()
