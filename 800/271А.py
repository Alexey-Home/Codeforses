"""Коасивый год"""

def main():
    n = int(input())
    while True:
        n += 1
        if len(str(n)) == len(set(str(n))):
            print(n)
            break



if __name__ == "__main__":
    main()
