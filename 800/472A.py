"""Уроки дизайна задач: учимся математики"""

def main():
    n = int(input())
    count = 4
    while True:
        if check_number(count) and check_number(n - count):
            print(count, n - count)
            break
        count += 1



def check_number(d):
    count = 0
    for i in range(1, d + 1):
        if d % i == 0:
            count += 1
        if count >= 3:
            return True
    return False

if __name__ == "__main__":
    main()