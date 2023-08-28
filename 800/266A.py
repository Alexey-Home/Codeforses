"""Камни на столе"""

def main():
    n = int(input())
    stone = list(input())
    count = 0
    for i in range(n-1):
        if stone[i] == stone[i+1]:
            count += 1
    print(count)

if __name__ == "__main__":
    main()