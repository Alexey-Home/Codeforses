"""Слоник"""


def main():
    n = int(input())
    count = 0
    trip = 0
    while n != 0:
        for i in [5, 4, 3, 2, 1]:
            if trip + i <= n:
                n = n - i
                count += 1
                break
    print(count)

if __name__ == "__main__":
    main()
