
def main():
    n = int(input())
    distance = [int(i) for i in input().split()]
    for _ in range(n):
        count = 0
        for i in range(1, len(distance)):
            if distance[i] - distance[0] > 0:
                count += 1
        print(count)

if __name__ == "__main__":
    main()