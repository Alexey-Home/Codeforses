"""В поисках простой задачи"""


def main():
    n = input()
    answer = list(input())
    print("HARD") if answer.count("1") > 0 else print("EASY")


if __name__ == "__main__":
    main()
