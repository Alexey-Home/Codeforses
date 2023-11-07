def main():
    import sys
    input=sys.stdin.readline
    for _ in range(int(input())):
      n,m=map(int,input().split())
      a=[*map(int,input().split())]
      s=[0]
      for i in range(n):s.append((s[-1]+a[i])%2)
      for _ in range(m):
        l,r,k=map(int,input().split())
        t=s[-1]-s[r]+s[l-1]+(r-l+1)*k
        print('YES'if t%2 else'NO')


if __name__ == "__main__":
    main()
