def main():
    t = int(input())
    result = []
    for i in range(t):
        n = int(input())
        words = list(input())
        tmp = []
        for i in range(n):
            if i == 0 or words[i] != words[i-1]:
                tmp.append(words[i])
        for i in tmp:
            if tmp.count(i) > 1:
                result.append("NO")
                break
        else:
            result.append("YES")
    print(*result, sep="\n")


if __name__ == "__main__":
    main()