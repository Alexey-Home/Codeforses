"""Панграмма"""

def main():
    t = int(input())
    n = input().lower()
    print("YES") if len(set(n)) == 26 else print("NO")


if __name__ == "__main__":
    main()
