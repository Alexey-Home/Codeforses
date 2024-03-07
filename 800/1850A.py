def main():
    n = int(input())
    for _ in range(n):
        arr = [int(i) for i in input().split()]
        arr = sorted(arr)
        print("YES") if arr[1] + arr[2] >= 10 else print("NO")

if __name__ == "__main__":
    main()