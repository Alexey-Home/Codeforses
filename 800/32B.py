"""Азбука Борзе"""

def main():
    n = input()
    n = n.replace("--", "2").replace("-.", "1").replace(".", "0")
    print(n)


if __name__ == "__main__":
    main()
