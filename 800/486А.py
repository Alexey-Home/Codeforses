"""Подсчет функции"""
import math


def main():
    n = int(input())
    if n % 2 == 0:
        print(int(n/2))
    else:
        print(-math.ceil(n/2))

if __name__ == "__main__":
    main()