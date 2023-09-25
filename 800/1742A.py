"""Сумма"""

def main():
    n = int(input())
    for _ in range(n):
        row = [int(i) for i in input().split()]
        maxx = row.pop(row.index(max(row)))
        if maxx == sum(row):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()