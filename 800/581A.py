"""Хипстер Вася"""


def main():
    a, b = [int(i) for i in input().split()]
    print(min(a, b), (max(a, b) - min(a, b)) // 2)


if __name__ == "__main__":
    main()
    