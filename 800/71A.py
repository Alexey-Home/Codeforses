"""Слишком длинные слова"""

def main():
    n = int(input())
    for i in range(n):
        word = input()
        if len(word) > 10:
            print(word[0] + str(len(word[1:-1:])) + word[-1])
        else:
            print(word)




if __name__ == "__main__":
    main()