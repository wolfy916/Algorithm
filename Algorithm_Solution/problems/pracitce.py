import sys

def input():
	return sys.stdin.readline().rstrip('\n')

def solution():
	def bfs(i, j):
		cnt = 1
		coords = [(i, j)]
		idx = 0
		while idx < len(coords):
			vi, vj = coords[idx]
			for di, dj in delta:
				ni, nj = vi + di, vj + dj
				if ni < 0 or nj < 0 or ni >= N or nj >= N: continue
				if board[ni][nj] != board[i][j] or visited[ni][nj]: continue
				cnt += 1
				visited[ni][nj] = True
				coords.append((ni, nj))
			idx += 1
		return cnt, coords

	for y, x, d in question:
		y, x = int(y) - 1, int(x) - 1
		board[y][x] = d
		visited = [[False] * N for _ in range(N)]
		for i in range(N):
			for j in range(N):
				if visited[i][j] or board[i][j] == '.': continue
				visited[i][j] = True
				cnt, coords = bfs(i, j)
				if cnt < K: continue
				for r, c in coords:
					board[r][c] = '.'

	return '\n'.join(map(''.join, board))

if __name__ == '__main__':
	N, K, Q = map(int, input().split())
	board = [list(input()) for _ in range(N)]
	question = [tuple(input().split()) for _ in range(Q)]
	delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	print(solution())