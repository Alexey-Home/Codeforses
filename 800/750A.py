"""Новый год и спешка"""

def main():
    n, k = [int(i) for i in input().split()]
    mul = 0
    time = 240 - k
    for i in range(1, n + 1):
        mul = mul + i * 5
        if mul > time:
            print(i - 1)
            break
    else:
        print(i)







if __name__ == "__main__":
    main()