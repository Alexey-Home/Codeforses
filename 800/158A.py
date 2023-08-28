"""Следующий раунд"""


def main():
    n, k = input().split(" ")
    score = input().split(" ")
    n, k = int(n), int(k)
    score = [int(i) for i in score]
    print(len([score[i] for i in range(n) if score[i] > 0 and score[i] >= score[k-1]]))


if __name__ == "__main__":
    main()