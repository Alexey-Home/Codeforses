"""Антон и многограники"""

def main():
    n = int(input())
    count = 0
    for _ in range(n):
        word = input()
        if word == "Tetrahedron":
            count += 4
        elif word == "Cube":
            count += 6
        elif word == "Octahedron":
            count += 8
        elif word == "Dodecahedron":
            count += 12
        elif word == "Icosahedron":
            count += 20
    print(count)



if __name__ == "__main__":
    main()
