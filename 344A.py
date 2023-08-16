"""Магниты"""

def main():
    n = int(input())
    o_q = "00"
    count = 0
    for _ in range(n):
        q = input()
        if o_q != q:
            count += 1
            o_q = q
    print(count)

if __name__ == "__main__":
    main()