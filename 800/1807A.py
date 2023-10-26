def main():
    n = int(input())
    for _ in range(n):
        a, b, c = list(map(int, input().split()))
        if a + b == c:
            print("+")
        else:
            print("-")

if __name__ == "__main__":
    main()