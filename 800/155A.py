"""I love username"""

def main():
    n = int(input())
    lst = [int(i) for i in input().split()]
    num_min = lst[0]
    num_max = lst[0]
    count = 0
    for i in lst:
        if num_min > i:
            count += 1
            num_min = i
        if num_max < i:
            count += 1
            num_max = i
    print(count)
if __name__ == "__main__":
    main()