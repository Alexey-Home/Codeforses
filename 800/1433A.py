def main():
    t = int(input())
    for _ in range(t):
        n = input()
        apartments = []
        for num in range(1, 10):
            for mul in range(1, 5):
                apartments.append(f"{num}" * mul)

        boring_ap = apartments[0:apartments.index(n) + 1]
        print(sum([len(i) for i in boring_ap]))

if __name__ == "__main__":
    main()