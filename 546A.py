"""Солдат и бананы"""

def main():
    k, n, w = [int(i) for i in input().split(" ")]
    summ = sum([k * i for i in range(1, int(w) + 1)])
    if summ - n > 0:
        print(summ-n)
    else:
        print(0)


if __name__ == "__main__":
    main()