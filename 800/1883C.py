def main():

    # with open("test.dat", "r") as file:
    #     input = file.readlines()
    # for i in range(len(input)):
    #     if input[i] == "\n" or i % 2 != 0:
    #         continue
    #
    #     n, k = list(map(int, input[i].split()))
    #     arr = list(map(int, input[i + 1].split()))

    n = int(input())
    for _ in range(n):
        n, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        count = 0
        multy = get_multy(arr)

        if multy % k == 0:
            print(0)
            continue
        if k == 5:
            five = [k - i for i in arr if i <= k]
            ten = [10 - i for i in arr]
            print(min(five + ten))
            continue

        arr2 = arr.copy()
        ex = False
        while True:
            if ex:
                print(count)
                break
            multy = get_number(k, multy)
            for i in range(len(arr2)):
                arr1 = increase(arr2.copy(), i)
                tmp = get_multy(arr1)
                if tmp % k == 0:
                    count += 1
                    ex = True
                    break
                elif get_multy(arr1) < multy:
                    arr2 = arr1.copy()
                    count += 1



def increase(arr, i):
    arr[i] = arr[i] + 1
    return arr



def get_multy(arr):
    multy = 1
    for a in arr:
        multy *= a
    return multy


def get_number(k, multy):
    if (multy + 1) % k == 0:
        return multy
    else:
        multy += 1
        while multy % k != 0:
            multy += 1
    return multy






if __name__ == "__main__":
    main()