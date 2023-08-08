"""Красивая матрица"""

def main():
    i, j = 0, 0
    for n in range(5):
        row = input().split()
        if row.count("1") == 1:
            j = row.index("1")
            i = n
            break
    print(abs(2 - j) + abs(2 - i))

if __name__ == "__main__":
    main()