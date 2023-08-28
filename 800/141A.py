"""Веселая шутка"""

def main():
    a = input()
    b = input()
    c = list(input())
    d = a + b
    for i in range(len(a) + len(b)):
        if d[i] in c:
            ind = c.index(d[i])
            c[ind] = ""
    if len(set(c)) == 1:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()