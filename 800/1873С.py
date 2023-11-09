def main():
    n = int(input())
    for _ in range(n):
        hits = []
        for i in range(0, 10):
            strng = input()
            for j in range(0, 10):
                if strng[j] == "X":
                    hits.append([i + 1, j + 1])
        count = 0
        for hit in hits:
            if hit[0] in [1, 10] or hit[1] in [1, 10]:
                count += 1
            elif (hit[0] in [2, 9] or hit[1] in [2, 9]) and (2 <= hit[0] <= 9 or 2 <= hit[0] <= 9):
                count += 2
            elif (hit[0] in [3, 8] or hit[1] in [3, 8]) and (3 <= hit[0] <= 8 or 3 <= hit[0] <= 8):
                count += 3
            elif (hit[0] in [4, 7] or hit[1] in [4, 7]) and (4 <= hit[0] <= 7 or 4 <= hit[0] <= 7):
                count += 4
            elif (hit[0] in [5, 6] or hit[1] in [5, 6]) and (5 <= hit[0] <= 6 or 5 <= hit[0] <= 6):
                count += 5

        print(count)


if __name__ == "__main__":
    main()