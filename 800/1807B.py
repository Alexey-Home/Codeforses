


def main():
    n = int(input())
    for _ in range(n):
        k = int(input())
        row = list(map(int, input().split()))

        m = []
        b = []

        for r in row:
            if r % 2 == 0:
                m.append(r)
            else:
                b.append(r)

        if sum(b) >= sum(m):
            print("NO")
        else:
            print("YES")





if __name__ == "__main__":
    main()