
def main():
    n = int(input())
    for _ in range(n):
        ticket = [int(i) for i in list(input())]
        if sum(ticket[0:3]) == sum(ticket[3:6]):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()