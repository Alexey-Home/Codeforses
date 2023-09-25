def main():
    n = int(input())
    lst = [int(i) for i in input().split()]
    count = min([lst.count(i) for i in range(1, 4)])
    print(count)
    for _ in range(count):
        tmp = []
        for i in range(1, 4):
            index = lst.index(i)
            tmp.append(index + 1)
            lst[index] = 0
        print(*tmp)


if __name__ == "__main__":
    main()