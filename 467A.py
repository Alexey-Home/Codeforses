"""Юра и заселение"""

def main():
    n = int(input())
    count = 0
    for _ in range(n):
        p, q = [int(i) for i in input().split()]
        if q - p >= 2:
            count += 1
    print(count)


if __name__ == "__main__":
    main()