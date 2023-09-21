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

def dfs():


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
	
	answer = float('inf')

	print(answer if answer < float('inf') else -1)