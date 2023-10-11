
def main():
    n = int(input())
    chris = 0
    mishka = 0
    for _ in range(n):
        score = [int(i) for i in input().split()]
        mishka += score[0]
        chris += score[1]
    if chris > mishka:
        print("Chris")
    elif chris < mishka:
        print("Mishka")
    else:
        print("Friendship is magic!^^")

if __name__ == "__main__":
    main()