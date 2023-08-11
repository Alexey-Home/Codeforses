
def main():
    n = int(input())
    score = input()

    d = score.count("D")
    a = score.count("A")
    if d > a:
        print("Danik")
    elif a > d:
        print("Anton")
    else:
        print("Friendship")

if __name__ == "__main__":
    main()