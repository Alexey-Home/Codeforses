"""Халк"""

def main():
    n = int(input())
    temp = "I hate {0}it"

    for i in range(n):
        if i == 0:
            strng = "{0}"
        elif i % 2 == 0:
            strng = "that I hate {0}"
        elif i % 2 != 0:
            strng = "that I love {0}"
        temp = temp.format(strng)
    else:
        temp = temp.format("")
    print(temp)



if __name__ == "__main__":
    main()