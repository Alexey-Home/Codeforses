def main():
    n = int(input())
    for _ in range(n):
        t = int(input())
        arr = list(map(int, input().split()))
        index = arr.index(min(arr))
        arr[index] += 1
        multi = 1
        for i in arr:
            multi *= i
        print(multi)

if __name__ == "__main__":
    main()