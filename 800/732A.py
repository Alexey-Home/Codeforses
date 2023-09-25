"""Куплю лопату"""


def main():
    k, r = [int(i) for i in input().split()]
    count = 1
    while True:
        if count * k % 10 == 0 or count * k - r % 10 == 0:
            print(count)
            break
        count += 1


if __name__ == "__main__":
    main()
