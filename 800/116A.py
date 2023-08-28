
def main():
    n = int(input())
    count = 0
    maxx = count
    for _ in range(n):
        a, b = [int(i) for i in input().split(" ")]
        count = count - a + b
        if maxx < count:
            maxx = count
    print(maxx)
    
if __name__ == "__main__":
    main()