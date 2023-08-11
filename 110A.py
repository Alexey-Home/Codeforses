"""Почти счастливое число"""

def main():
    n = input()
    print("YES") if n.count("4") + n.count("7") in [4, 7] else print("NO")



if __name__ == "__main__":
    main()

