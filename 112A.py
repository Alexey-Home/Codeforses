"""Петя и строки"""

def main():
    first_str = input().lower()
    second_str = input().lower()
    for i in range(len(first_str)):
        if first_str[i] != second_str[i]:
            if ord(first_str[i]) < ord(second_str[i]):
                print(-1)
                break
            elif ord(first_str[i]) > ord(second_str[i]):
                print(1)
                break
    else:
        print(0)

if __name__ == "__main__":
    main()