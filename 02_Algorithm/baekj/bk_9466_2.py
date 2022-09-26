# 텀 프로젝트
# 모범답안
from sys import stdin
input = stdin.readline


def dfs(x):
    global result
    test.append(x)
    visited[x] = 1
    y = arr[x]
    while True:
        if visited[y]:
            if y in test:
                result += test[test.index(y):]
            return
        else:
            visited[y] = 1
            test.append(y)
            y = arr[y]


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0]*(N+1)
    result = []

    for i in range(1, N+1):
        if not visited[i]:
            test = []
            dfs(i)

    print(N - len(result))