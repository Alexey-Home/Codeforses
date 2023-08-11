"""Неправильное вычитание"""


def main():
    num, n = input().split()
    for _ in range(int(n)):
        if num[-1] == "0":
            num = num[0:-1:]
        else:
            num = str(int(num) - 1)
    print(num)


if __name__ == "__main__":
    main()
