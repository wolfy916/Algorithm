# 회전 초밥
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [main]
if __name__ == '__main__':
    N, d, k, c = map(int, input().split())
    plates = [int(input()) for _ in range(N)]

    # 초기 세팅
    sushi = [0] * (d + 1)
    total = 0
    p1, p2 = 0, k - 1
    for i in range(k):
        if sushi[plates[i]] == 0:
            total += 1
        sushi[plates[i]] += 1

    # 투 포인터
    answer = total
    while p1 < N:
        sushi[plates[p1]] -= 1
        if sushi[plates[p1]] == 0:
            total -= 1
        p1 += 1
        p2 = (p2 + 1) % N
        sushi[plates[p2]] += 1
        if sushi[plates[p2]] == 1:
            total += 1
        answer = max(answer, total if sushi[c] else total + 1)

    print(answer)