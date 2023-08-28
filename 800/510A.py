"""Лиса и змейка"""

def main():
    n, m = [int(i) for i in input().split(" ")]
    t = -1
    for i in range(1, n + 1):
        if i % 2 == 0:
            tmp = list("." * m)
            tmp[t] = "#"
            print("".join(tmp))
            if t == -1:
                t = 0
            else:
                t = -1
        else:
            print("#" * m)


if __name__ == "__main__":
    main()