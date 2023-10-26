def main():
    t = int(input())
    for _ in range(t):
        n, k = [int(i) for i in input().split()]
        word = list(input())
        count = [word.count(i) for i in word]
        print(count)


        if word == word[::-1]:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()