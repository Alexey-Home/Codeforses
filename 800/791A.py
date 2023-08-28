"""Мишка и старший брат"""

def main():
    a, b = input().split()
    a, b = int(a), int(b)
    count = 0
    while a <= b:
        a = a*3
        b = b*2
        count += 1

    print(count)


if __name__ == "__main__":
    main()