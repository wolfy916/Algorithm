# 쉬운 최단거리
import sys
from collections import deque as dq

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] bfs 함수
def bfs(N, M, area, si, sj):
    # 데이터 초기화
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    INF = float('inf')  # 거리를 기록할 2차원 배열의 초기 원소값
    visited = [[INF] * M for _ in range(N)]
    visited[si][sj] = 0  # 초기 위치 설정
    q = dq([(si, sj)])   #

    # 탐색 시작
    while q:
        vi, vj = q.popleft()
        for di, dj in delta:
            ni, nj = vi + di, vj + dj
            # 인덱스 유효성 검사
            if ni < 0 or nj < 0 or ni >= N or nj >= M: continue
            # 해당 지점을 더 짧은 거리로만 갈 수 있도록 설정
            if visited[vi][vj] + 1 >= visited[ni][nj]: continue
            # 갈 수 있는 곳만 탐색
            if area[ni][nj] == 0: continue
            visited[ni][nj] = visited[vi][vj] + 1
            q.append((ni, nj))

    # 도달하지 못한 곳에 대한 처리
    for i in range(N):
        for j in range(M):
            if visited[i][j] != INF: continue
            visited[i][j] = 0 if area[i][j] == 0 else -1

    return visited

if __name__ == '__main__':
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]

    # 목표 지점에서 탐색 시작
    for i in range(N):
        for j in range(M):
            if area[i][j] == 2:
                visited = bfs(N, M, area, i, j)
                for i in range(N):
                    print(*visited[i])
                exit()