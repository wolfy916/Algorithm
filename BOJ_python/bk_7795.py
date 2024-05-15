# 먹을 것인가 먹힐 것인가

from sys import stdin

# [A] 입력 초기화
def input():
    return stdin.readline().rstrip('\n')

TC = int(input())
for _ in range(TC):
    # [1] 입력
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))  # 오름차순 정렬
    B = sorted(list(map(int, input().split())))  #

    # [2] 투 포인터
    a = b = cnt = 0
    while a < N and b < M:
        if A[a] > B[b]:
            b += 1
        else:
            a += 1
            cnt += b

    cnt += (N - a) * M  # 모든 B보다 큰 A들에 대한 카운팅

    print(cnt)