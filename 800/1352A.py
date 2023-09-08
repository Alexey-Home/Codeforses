"""Сумма круглых чисел"""

def main():
    n = int(input())
    for _ in range(n):
        number = int(input())
        num = 10
        rez = []
        for i in range(4):
            t = (number // num) % 10
            if t != 0:
               rez.append(((number // num) % 10) * num)
            num = num * 10

        else:
            if number % 10 != 0:
                rez.append(number % 10)
        print(len(rez))
        print(*rez)

if __name__ == "__main__":
    main()