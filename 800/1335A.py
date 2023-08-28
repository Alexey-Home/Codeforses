"""Конфеты и две сестры"""

def main():
    n = int(input())
    for _ in range(n):
        k = int(input())
        if k % 2 == 0:
            print(k // 2 - 1)
        else:
            print(k // 2)



if __name__ == "__main__":
    main()