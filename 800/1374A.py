def main():
    n = int(input())
    for _ in range(n):
        x, y, n = [int(i) for i in input().split()]
        div = n // x
        res = 0
        while div != 0:
            res = div * x + y
            if res < n:
               break
            div -= 1
        print(res)

if __name__ == "__main__":
    main()