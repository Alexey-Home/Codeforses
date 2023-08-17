
def main():
    n = int(input())
    for _ in range(n):
        a, b = [int(i) for i in input().split()]
        cel = a // b
        if a % b != 0:
            t = (cel + 1) * b
            print(t - a)
        else:
            print(0)

if __name__ == "__main__":
    main()