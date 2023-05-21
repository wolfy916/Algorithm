# 입국 심사

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [int(input()) for _ in '_' * N]
INF = 10**9  # 1명이 걸릴 수 있는 최대 심사 시간

start = 1       # 1초
end = M * INF   # (M명 * 10억)초
minV = M * INF  #
while start <= end:
    mid = (start + end) // 2

    people = 0  # 심사에 통과한 사람수
    for i in range(N):
        people += mid // lst[i]

    # mid[초] 동안 모든 심사대를 돌려도 M명을 심사할 수 없다면
    if people < M:
        start = mid + 1  # 시간을 늘림

    # M명 이상 심사했다면 최소 시간 갱신 시도
    else:
        minV = min(minV, mid)
        end = mid - 1  # 시간을 줄임

print(minV)
