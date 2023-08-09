"""Девушка или Юноша"""
def main():
    n = set(list(input()))
    if len(n) % 2 != 0:
        print("IGNORE HIM!")
    else:
        print("CHAT WITH HER!")

if __name__ == "__main__":
    main()
