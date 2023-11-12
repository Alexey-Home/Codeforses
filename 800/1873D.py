def main():
    n = int(input())
    for _ in range(n):
        n, k = list(map(int, input().split()))
        strip = input()
        # k = 2
        # strip = "WBBWBBWBBW"
        strip = list(strip)

        count = 0
        while True:
            if any(e in "B" for e in strip):
                index = strip.index("B")
                del strip[index:index + k]
                # len_slice = len(strip[index:index + k])
                # strip = strip[:index] + "W" * len_slice + strip[index + k:]
                count += 1
            else:
                break
        print(count)










if __name__ == "__main__":
    main()