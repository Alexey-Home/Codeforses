def main():
    n = int(input())
    for i in range(n):
        count_fields = int(input())
        count = []
        for num in range(count_fields):
            field = input()
            count_unit = field.count("1")
            if count_unit != 0:
                count.append(count_unit)

        print("SQUARE" if len(set(count)) == 1 else "TRIANGLE")



if __name__ == "__main__":
    main()