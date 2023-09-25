
def main():
    n = int(input())
    cards = [int(i) for i in input().split()]
    score = [0, 0]
    index = 1
    while len(cards) != 0:
        if index == 1:
            index = 0
        else:
            index = 1
        if cards[0] > cards[-1]:
            score[index] = score[index] + cards.pop(0)
        else:
            score[index] = score[index] + cards.pop(-1)
    print(*score)

if __name__ == "__main__":
    main()