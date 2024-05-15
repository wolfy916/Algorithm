'''
2024 카카오 테크 인턴십 4번문제
분류 :
'''

def solution(coin, cards):
    def dfs(turn, myCoin, nxt):
        nonlocal answer, n
        print("라운드", turn, "----------------")
        answer = max(answer, turn)
        if nxt >= n: return
        new1, new2 = cards[nxt], cards[nxt + 1]
        print(myCards)
        print("남은 코인: ", myCoin)
        print("뽑을 카드: ", new1, new2)
        myCards[new1] = True
        myCards[new2] = True
        for c in range(1, n // 2 + 1):
            if myCards[c] and myCards[n + 1 - c]:
                print(c, n+1-c)
                myCards[c] = False
                myCards[n + 1 - c] = False
                b1 = b2 = False
                if c == new1 or n + 1 - c == new1: b1 = True
                if c == new2 or n + 1 - c == new2: b2 = True
                if b1 and b2 and myCoin > 1:
                    dfs(turn + 1, myCoin - 2, nxt + 2)
                elif b1 and not b2 and myCoin > 0:
                    myCards[new2] = False
                    dfs(turn + 1, myCoin - 1, nxt + 2)
                    myCards[new2] = True
                    dfs(turn + 1, myCoin - 2, nxt + 2)
                elif not b1 and b2 and myCoin > 0:
                    myCards[new1] = False
                    dfs(turn + 1, myCoin - 1, nxt + 2)
                    myCards[new1] = True
                    dfs(turn + 1, myCoin - 2, nxt + 2)
                elif not b1 and not b2:
                    myCards[new1] = False
                    myCards[new2] = False
                    dfs(turn + 1, myCoin, nxt + 2)
                    myCards[new1] = True
                    myCards[new2] = True
                myCards[c] = True
                myCards[n + 1 - c] = True
        myCards[new1] = False
        myCards[new2] = False

    answer = 1
    n = len(cards)
    myCards = [False] * (n + 1)
    for i in range(n // 3):
        myCards[cards[i]] = True

    dfs(1, coin, n // 3)

    return answer

coins = [4, 3, 2, 10]
cards = [
    [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4],
    [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12],
    [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
]
correct = [5, 2, 4, 1]

if __name__ == '__main__':
    for i in [0]:
        print('------case', i+1)
        answer = solution(coins[i], cards[i])
        print('나의 답: ', answer)
        print('정답: ', correct[i])