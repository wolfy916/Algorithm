# 노드사이의 거리
import sys
from collections import deque as dq

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 노드 사이의 거리를 리턴하는 함수
def distance(a, b):
    visited = [False] * (N + 1)
    visited[a] = True
    q = dq([(a, 0)])
    while q:
        v, c = q.popleft()
        if v == b:
            return c
        for w, cost in adjL[v]:
            if visited[w]: continue
            visited[w] = True
            q.append((w, c + cost))

# [main]
if __name__ == '__main__':
    N, M = map(int, input().split())
    adjL = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b, c = map(int, input().split())
        adjL[a].append((b, c))
        adjL[b].append((a, c))

    for _ in range(M):
        a, b = map(int, input().split())
        print(distance(a, b))