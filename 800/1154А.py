"""Востановление трех чисел"""


def main():
    lst = [int(i) for i in input().split()]
    maxx = lst.pop(lst.index(max(lst)))
    a = lst[1] + lst[2] - maxx
    b = lst[1] - a
    c = lst[2] - a
    print(a, b, c)




if __name__ == "__main__":
    main()