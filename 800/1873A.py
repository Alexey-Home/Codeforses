def main():
    n = int(input())
    for _ in range(n):
        triger = False
        constnt = "abc"
        word = list(input())
        for i in range(len(word)):
            if triger:
                break
            for j in range(i, len(word)):
                tmp = word.copy()
                tmp[i], tmp[j] = tmp[j], tmp[i]
                if "".join(tmp) == constnt:
                    print("YES")
                    triger = True
                    break
        else:
            print("NO")






if __name__ == "__main__":
    main()