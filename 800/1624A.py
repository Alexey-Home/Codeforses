def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = [int(i) for i in input().split()]
        print(max(lst) - min(lst))


if __name__ == "__main__":
    main()