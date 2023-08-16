"""I Wanna be the Guy"""

def main():
    n = int(input())
    t = set(input().split() + input().split())
    t = list(t)
    if t.count("0") > 0:
        t.pop(t.index("0"))
    t = len(t)

    if t == n:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")



if __name__ == "__main__":
    main()