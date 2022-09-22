import sys
input = sys.stdin.readline

N = int(input())
cards = [int(input()) for _ in '_' * N]
cards.sort()

sumV = cards.pop(0) + cards.pop(0)
result = sumV
lenV = len(cards)
while cards:
    if cards[-1] < sumV:
        cards.append(sumV)
        lenV += 1
    else:
        cards = [sumV] + cards
        lenV += 1
        for i in range(lenV - 1):
            if cards[i] > cards[i+1]:
                cards[i], cards[i+1] = cards[i+1], cards[i]
            else:
                break
    sumV = cards.pop(0) + cards.pop(0)
    lenV -= 2
    result += sumV

print(result)