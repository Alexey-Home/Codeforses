"""Yes или Yes?"""


def main():
    n = int(input())
    for _ in range(n):
        word = input()
        if word.lower() == "yes":
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()