def main():
    n = int(input())
    row = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


    for _ in range(n):
        pin = [int(i) for i in list(input())]
        index = 0
        count = 0
        for i in pin:
            while True:
                if row.index(i) < index:
                    step = -1
                else:
                    step = 1
                if i == row[index]:
                    count += 1
                    break
                else:
                    index += step
                    count += 1
        print(count)



if __name__ == "__main__":
    main()