"""Bit++"""
import re

def main():
    n = int(input())
    x = 0
    for i in range(n):
        opr = input()
        if re.compile(r"^[-]*X[-]*$").match(opr):
            x -= 1
        else:
            x += 1
    print(x)


if __name__ == "__main__":
    main()