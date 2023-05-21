# 적록색약
# 풀이가 너무 마음에 안든다..
# 더 좋은 방법이 있을것같은데 모르겠음

N = int(input())
area = [list(input()) for _ in '_'*N]

visited = [[0]*N for _ in '_'*N]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
normal = problem = 0

# [1] R, G, B를 모두 탐색하며,
#     visited를 R, G일때는 1, B일때는 -1로 기록
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            if area[i][j] == 'B':
                color = -1
                problem += 1  # Blue 색상은 색약도 볼 수 있어서 카운트
            else:
                color = 1
            q = [(i, j)]
            visited[i][j] = color
            while q:
                vi, vj = q.pop(0)
                for di, dj in delta:
                    ni, nj = vi+di, vj+dj
                    if 0 <= ni < N and 0 <= nj < N:
                        if not visited[ni][nj] and area[i][j] == area[ni][nj]:
                            visited[ni][nj] = color
                            q.append((ni, nj))
            normal += 1  # 평범한 사람은 모든 색상을 볼 수 있어서 카운트

# [2] visited = 1로 연결된 구역의 수를 카운트
for i in range(N):
    for j in range(N):
        if visited[i][j] == 1:
            q = [(i, j)]
            visited[i][j] = 2
            while q:
                vi, vj = q.pop(0)
                for di, dj in delta:
                    ni, nj = vi + di, vj + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        if visited[ni][nj] == 1:
                            visited[ni][nj] = 2
                            q.append((ni, nj))
            problem += 1

print(normal, problem)