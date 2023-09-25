
def main():
    n = int(input())
    for _ in range(n):
        strng = list(input())
        lenght = len(strng)
        i = 0
        while i < lenght - 1:
            if strng[i] == strng[i + 1]:
                strng.pop(i)
                lenght = len(strng)
            i += 1
        print("".join(strng))



if __name__ == "__main__":
    main()