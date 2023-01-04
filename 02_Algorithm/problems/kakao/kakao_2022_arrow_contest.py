# 양궁 대회

n = 10
info = [0,0,0,0,0,0,0,0,3,4,3]

def solution(n, info):
    result = -1
    possible_lst = []
    enemy = 0
    for i, cnt in enumerate(info):
        if cnt:
            enemy += 10 - i
        possible_lst.append([cnt + 1, 10 - i])

    from itertools import combinations as cb
    for i in range(1, n+1):
        combs = list(cb(possible_lst, i))
        for comb in combs:
            sumV = 0
            enemy_total = enemy
            total = 0
            for cnt, point in comb:
                sumV += cnt
                total += point
                if info[10-point]:
                    enemy_total -= point
            if sumV > n:
                continue
            else:
                if enemy_total >= total:
                    continue
                else:
                    temp = [0]*11
                    for c, p in comb:
                        temp[10 - p] = c
                    if result < total - enemy_total:
                        result = total - enemy_total
                        answer = temp[:]
                        if n - sumV > 0:
                            answer[10] = n - sumV
                    elif result == total - enemy_total:
                        for j in range(10, -1, -1):
                            if answer[j] > temp[j]:
                                break
                            elif answer[j] < temp[j]:
                                answer = temp[:]
                                break
    if result == -1:
        answer = [-1]
    return answer

print(solution(n, info))