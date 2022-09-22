# 신입사원

from sys import stdin
input = stdin.readline

for _ in '_'*int(input()):
    N = int(input())
    arr = [0] * (N+1)
    for i in range(N):
        a, b = map(int, input().split())
        arr[a] = b
    cnt = 0
    for j in range(1, N):
        for k in range(j+1, N-1):
            if arr[j] > arr[k]:
                cnt += 1
                break
    print(N-cnt)