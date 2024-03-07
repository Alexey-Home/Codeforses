def main():
    n = int(input())
    for i in range(n):
        word = input()
        print("A" if word.count("A") > word.count("B") else "B")


if __name__ == "__main__":
    main()