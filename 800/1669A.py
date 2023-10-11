
def main():
    n = int(input())

    for _ in range(n):
        rating = int(input())
        if 1900 <= rating:
            res = "1"
        elif 1600 <= rating <= 1899:
            res = "2"
        elif 1400 <= rating <= 1599:
            res = "3"
        else:
            res = "4"
        print(f"Division {res}")

if __name__ == "__main__":
    main()