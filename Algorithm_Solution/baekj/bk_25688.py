# 빠른 무작위 숫자 탐색
import sys


# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')


# [B] bfs, 임의의 자연수 a -> b로 가는 거리를 간선의 가중치로 표기
def bfs(si, sj):
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * 5 for _ in range(5)]
    visited[si][sj] = True
    q = [(si, sj, 0)]
    while q:
        vi, vj, cnt = q.pop(0)
        if board[vi][vj] > 0:
            adjM[board[si][sj]][board[vi][vj]] = cnt
            adjM[board[vi][vj]][board[si][sj]] = cnt
        for di, dj in delta:
            ni, nj = vi + di, vj + dj
            if ni < 0 or nj < 0 or ni >= 5 or nj >= 5: continue
            if visited[ni][nj] or board[ni][nj] == -1: continue
            visited[ni][nj] = True
            q.append((ni, nj, cnt + 1))


# [C] dfs, r, c에서 출발한 최소 거리 계산
def dfs(v, d):
    global answer
    if visited.count(True) == 7:
        answer = min(answer, d)
        return
    for w in range(1, 7):
        if visited[w] or d + adjM[v][w] >= answer: continue
        visited[w] = True
        dfs(w, d + adjM[v][w])
        visited[w] = False


# [main]
if __name__ == "__main__":
    # 입력부
    board = [list(map(int, input().split())) for _ in range(5)]
    r, c = map(int, input().split())

    # 자연수가 표기되어있는 숫자판의 좌표 기록
    coords = [[] for _ in range(7)]
    coords[0] = [r, c]
    for i in range(5):
        for j in range(5):
            if board[i][j] < 1: continue
            coords[board[i][j]] = [i, j]

    # 인접행렬 생성 및 거리 기록
    INF = float('inf')
    adjM = [[INF] * 7 for _ in range(7)]
    for i in range(6):
        si, sj = coords[i]
        bfs(si, sj)

    # dfs 백트랙킹 탐색을 위한 visited 생성
    visited = [False] * 7
    visited[0] = True
    for i in range(1, 7):
        if adjM[0][i] == 0:
            visited[i] = True  # 출발지인 r, c에 자연수가 기록되어있는 경우

    answer = INF
    dfs(0, 0)
    print(answer if answer < INF else -1)