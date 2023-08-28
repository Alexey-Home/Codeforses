"""Антон и буквы"""
import re

def main():
    n = input()[1:-1].split(", ")
    print(len(set(n)))

if __name__ == "__main__":
    main()