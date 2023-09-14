# 운동
import sys

# [A] 입력 함수 초기화
def input():
	return sys.stdin.readline().rstrip('\n')

# [main]
if __name__ == '__main__':
	V, E = map(int, input().split())
	edges = [tuple(map(int, input().split())) for _ in range(E)]

	INF = float('inf')
	adjM = [[INF] * (V + 1) for _ in range(V + 1)]

	for a, b, c in edges:
		adjM[a][b] = c

	for r in range(1, V + 1):
		for s in range(1, V + 1):
			for e in range(1, V + 1):
				adjM[s][e] = min(adjM[s][e], adjM[s][r] + adjM[r][e])

	answer = float('inf')
	for i in range(1, V + 1):
		answer = min(answer, adjM[i][i])

	print(answer if answer < INF else -1)