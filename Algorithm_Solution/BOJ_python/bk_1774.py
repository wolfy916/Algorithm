# 우주신과의 교감
import sys
from heapq import heappush, heappop

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 좌표간 거리 계산
def dis(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

# [C] 인접 행렬 생성
def make_adjM(N, gods, connects):
    adjM = [[0] * N for _ in range(N)]
    # [C-1] 좌표 간의 간선 및 가중치 표기
    for i in range(N - 1):
        x1, y1 = gods[i]
        for j in range(i + 1, N):
            x2, y2 = gods[j]
            d = dis(x1, y1, x2, y2)
            adjM[i][j] = d
            adjM[j][i] = d
    # [C-2] 이미 연결된 간선들의 가중치를 0처리
    for a, b in connects:
        adjM[a - 1][b - 1] = 0
        adjM[b - 1][a - 1] = 0
    return adjM

# [D] MST prim 함수
def prim(N, gods, connects):
    adjM = make_adjM(N, gods, connects)
    visited = [False] * N
    q = [(0, 0)]
    cost = 0
    while q:
        c, v = heappop(q)
        if visited[v]: continue
        visited[v] = True
        cost += c ** 0.5
        for w in range(N):
            if v == w or visited[w]: continue
            heappush(q, (adjM[v][w], w))
    return round(cost, 3)

# [main]
if __name__ == '__main__':
    N, M = map(int, input().split())
    gods = [tuple(map(int, input().split())) for _ in range(N)]
    connects = [tuple(map(int, input().split())) for _ in range(M)]
    print(f'{prim(N, gods, connects):.2f}')