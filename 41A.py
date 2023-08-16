
def main():
    word = input()
    drow = input()
    if word[-1:-len(word) - 1:-1] == drow:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()