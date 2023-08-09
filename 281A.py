"""Капитализация слова"""

def main():
    n = input()
    n = n[0].upper() + n[1:len(n):1]
    print(n)

if __name__ == "__main__":
    main()