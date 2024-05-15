# 9937. 5203. 베이비진 게임
def run(arr, len_v):
    cnt_list = [0] * len_v
    for e in arr:
        cnt_list[e] += 1
    for cnt in cnt_list:
        if cnt >= 3:
            return 1
    return 0


def triplet(arr, len_v):
    cnt_list = [0] * len_v
    for e in arr:
        cnt_list[e] += 1
    for j in range(len_v-3):
        if cnt_list[j] and cnt_list[j+1] and cnt_list[j+2]:
            return 1
    return 0


for tc in range(1, int(input())+1):
    player1 = []
    player2 = []
    cards = list(map(int, input().split()))
    n = len(cards)

    result = 0
    for i in range(n):
        if i % 2:
            player2 += [cards[i]]
            len_v2 = len(player2)
            if len_v2 >= 3:
                if run(player2, n) or triplet(player2, n):
                    result = 2
                    break
        else:
            player1 += [cards[i]]
            len_v1 = len(player1)
            if len_v1 >= 3:
                if run(player1, n) or triplet(player1, n):
                    result = 1
                    break

    print(f'#{tc} {result}')
