"""Ваня и забор"""

def main():
    n, h = [int(i) for i in input().split()]
    row = [int(i) for i in input().split()]
    tmp = [1 if i <= h else 2 for i in row]
    print(sum(tmp))

if __name__ == "__main__":
    main()