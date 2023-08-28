"""Выиграть в лотерею"""

def main():
    n = int(input())
    count = 0
    while n != 0:
        for i in [100, 20, 10, 5, 1]:
            t = n // i
            if n // i > 0:
                count += t
                n -= t*i
                break
    print(count)


if __name__ == "__main__":
    main()