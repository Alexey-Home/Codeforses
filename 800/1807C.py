def main():
    n = int(input())
    for _ in range(n):
        t = int(input())
        word = list(input())
        let = {}
        val = 0
        for i in range(len(word)):
            if word[i] not in let:
                let[word[i]] = val
            word[i] = let[word[i]]
            if i % 2 == 0:
                val = 1
            else:
                val = 0
            if i != 0 and word[i] == word[i - 1]:
                print("NO")
                break
        else:
            print("YES")



if __name__ == "__main__":
    main()