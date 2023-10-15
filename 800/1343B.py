
def main():
    n = int(int(input())/2)
    if n == 1:
        print("NO")
        return
    count = 0
    even = []
    for i in range(n):
        count += 2
        even.append(count)


    summ = sum(even)
    odd = []
    count = -1
    for i in range(n):
        count += 2
        odd.append(count)
        summ -= count
    else:
        if sum(odd) != sum(even):
            odd[-1] = odd[-1] + summ
            if sum(odd) != sum(even):
                print("NO")
            else:
                print("YES")
                print(even + odd)
        else:
            print("YES")
            print(even + odd)





if __name__ == "__main__":
    main()