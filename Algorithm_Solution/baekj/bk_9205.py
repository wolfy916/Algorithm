# 맥주 마시면서 걸어가기
import sys
from collections import deque as dq

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 맨해튼 거리 계산 함수
def dis(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# [C] 메인 로직 함수
def solution(n, coords):
    # 인접 행렬에 양방향 간선 표기
    INF = float('inf')
    adjM = [[INF] * (n + 2) for _ in range(n + 2)]
    for i in range(n + 1):
        for j in range(i + 1, n + 2):
            d = dis(coords[i][0], coords[i][1], coords[j][0], coords[j][1])
            adjM[i][j] = d
            adjM[j][i] = d

    # bfs
    visited = [False] * (n + 2)
    visited[0] = True
    q = dq([0])
    while q:
        v = q.popleft()
        # 맥주 20캔으로 도착지까지 갈 수 있으면 참
        if adjM[v][n + 1] <= 1000:
            return 'happy'
        for w in range(n + 2):
            if visited[w]: continue
            if adjM[v][w] > 1000: continue
            visited[w] = True
            q.append(w)
    return 'sad'

# [main]
if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        n = int(input())
        coords = [tuple(map(int, input().split())) for _ in range(n + 2)]
        print(solution(n, coords))
