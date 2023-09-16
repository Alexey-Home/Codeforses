def main():
    n, k, l, c, d, p, nl, np = [int(i) for i in input().split()]
    all_mm = k * l // nl
    all_liam = c * d
    salt = p // np
    print(min(all_mm, all_liam, salt)//n)


if __name__ == "__main__":
    main()