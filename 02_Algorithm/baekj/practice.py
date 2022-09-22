# 카드 정렬하기

import sys
input = sys.stdin.readline

N = int(input())
cards = [int(input()) for _ in '_' * N]
cards.sort()

sumV = cards.pop(0) + cards.pop(0)
result = sumV

while cards:
    cards = [sumV] + cards
    for i in range(len(cards)-1):
        if cards[i] > cards[i+1]:
            cards[i], cards[i+1] = cards[i+1], cards[i]
    sumV = cards.pop(0) + cards.pop(0)
    result += sumV

print(result)