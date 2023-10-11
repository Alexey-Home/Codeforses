
def main():
    def check_num(num):
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
            if count == 3:
                return True
        return False

    n = int(input())
    y = 2
    while n != 0:
        x = n - y
        if check_num(x) and check_num(y):
            print(x, y)
            break
        else:
            y += 1


if __name__ == "__main__":
    main()