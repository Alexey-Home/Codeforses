
def main():
    n = int(input())
    lst = [int(i) for i in input().split()]
    count = 0
    ind_min = 0
    ind_max = -1
    for i in range(len(lst)):
        if lst[i] == min(lst):
            ind_min = i
    for i in range(ind_min, len(lst) - 1):
        if lst[i] == min(lst) and lst[i] < lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            count += 1
        if lst[-1] == min(lst):
            break
    for i in range(-1, -len(lst) - 1, -1):
        if lst[i] == max(lst):
            ind_max = i
    for i in range(ind_max, -len(lst), -1):
        if lst[i] == max(lst) and lst[i] > lst[i - 1]:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            count += 1
        if lst[0] == max(lst):
            break
    print(count)


if __name__ == "__main__":
    main()