"""Новый год: встреча друзей"""


def main():
    lst = [int(i) for i in input().split()]
    c_max = lst.pop(lst.index(max(lst)))
    c_min = lst.pop(lst.index(min(lst)))
    c_middle = lst[0]
    rez = abs(c_middle - c_max) + abs(c_middle - c_min)
    print(rez)


if __name__ == "__main__":
    main()