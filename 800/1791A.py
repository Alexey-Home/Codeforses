def main():
    n = int(input())
    for _ in range(n):
        letter = input()
        if letter.lower() in "codeforces":
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()