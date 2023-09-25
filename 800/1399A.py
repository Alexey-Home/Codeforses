"""Удалить наименьшее"""

def main():
    n = int(input())
    for _ in range(n):
        k = int(input())
        lst = [int(j) for j in input().split()]
        i = 0
        lenght = len(lst)
        while i != lenght - 1:
            j = i + 1
            while j != lenght:
                if abs(lst[i] - lst[j]) <= 1:
                    lst.pop(lst.index(min(lst[i], lst[j])))
                    lenght = len(lst)
                    i = 0
                    break
                j += 1
            else:
                i += 1

        if len(lst) == 1:
            print("YES")
        else:
            print("NO")




if __name__ == "__main__":
    main()