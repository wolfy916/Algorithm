# 행성 연결
import sys
from heapq import heappush, heappop

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] MST prim
def prim(N, adjM):
    q = []
    heappush(q, (0, 0))  # 출발지 설정
    visited = [False] * N
    cost = 0
    while q:
        c, v = heappop(q)
        if visited[v]: continue
        visited[v] = True
        cost += c
        for w in range(N):
            if adjM[v][w] == 0: continue
            if visited[w]: continue
            heappush(q, (adjM[v][w], w))
    return cost

# [main]
if __name__ == '__main__':
    N = int(input())
    adjM = [list(map(int, input().split())) for _ in range(N)]
    print(prim(N, adjM))