"""Праздник равенства"""

def main():
    n = int(input())
    lst = [int(i) for i in input().split()]
    print(sum([max(lst) - i for i in lst]))

if __name__ == "__main__":
    main()