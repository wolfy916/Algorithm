# 신입사원

from sys import stdin
input = stdin.readline

for _ in '_'*int(input()):
    N = int(input())
    arr = [0] * (N+1)
    for i in range(N):
        a, b = map(int, input().split())
        arr[a] = b
    cnt = 1
    c = arr[1]
    for j in range(2, N+1):
        if c > arr[j]:
            c = arr[j]
            cnt += 1
    print(cnt)