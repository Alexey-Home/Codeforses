"""Магниты"""
import time

def main():
    st = time.time()
    n = int(input())
    arr = ["00"] * n
    for i in range(n):
        arr[i] = input()
    plus = arr.count("01")
    minus = arr.count("10")
    temp = "".join(arr)
    if plus > minus:
        temp = temp.split("10")
    else:
        temp = temp.split("01")



    et = time.time()


    print(et - st)

    print("f")

if __name__ == "__main__":
    main()