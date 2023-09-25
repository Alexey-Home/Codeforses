def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = input().split()
        i, j = set(lst)
        if lst.count(i) <= 1:
            print(lst.index(i) + 1)
        else:
            print(lst.index(j) + 1)


if __name__ == "__main__":
    main()