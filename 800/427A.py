"""Полицейские рекруты"""

def main():
    n = int(input())
    t = [int(i) for i in input().split()]
    count = 0
    summ = 0
    for i in t:
        summ += i
        if summ < 0:
            count += 1
            summ = 0
    print(count)


if __name__ == "__main__":
    main()