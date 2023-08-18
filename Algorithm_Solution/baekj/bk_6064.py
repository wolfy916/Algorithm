# 풀이 1. 완전 탐색
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

TC = int(input())
for _ in range(TC):
    M, N, x, y = map(int, input().split())
    if M > N:
        M, N = N, M
        x, y = y, x
    elif M == N:
        print(-1 if x != y else y)
        continue
    answer = y
    limit = N * M
    differ = abs(N - M)
    a = b = y
    if y > M:
        a = y % M if y % M else M
    while (a, b) != (x, y) and answer <= limit:
        a += differ
        if a > M:
            a = a % M if a % M else M
        answer += N
    print(answer if answer <= limit else -1)