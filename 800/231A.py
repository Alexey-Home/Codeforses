"""Команда"""

def main():
    n = int(input())
    count = 0
    for i in range(n):
        txt_in = input()
        temp = txt_in.split(" ")
        if temp.count("1") >= 2:
            count += 1
    print(count)

if __name__ == "__main__":
    main()