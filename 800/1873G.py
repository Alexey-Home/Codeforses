def main():
    n = int(input())
    for _ in range(n):
        n, x = list(map(int, input().split()))
        arr = [int(i) for i in input().split()]
        lengnt = len(arr)
        summ = sum(arr)
        all = summ + x
        h = int(all / lengnt)



        while h != 0:
            sm = 0
            for i in arr:
                if i > h:
                    sm += h
                else:
                    sm += i
            all = h * lengnt
            volume = all - sm

            if volume <= x:
                print(h)
                break
            h -= 1






if __name__ == "__main__":
    main()