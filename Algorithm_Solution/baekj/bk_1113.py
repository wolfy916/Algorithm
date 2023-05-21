# 수영장 만들기

N, M = map(int, input().split())
ground = [list(map(int, list(input()))) for _ in '_'*N]

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = 0
for w_h in range(2, 10):  # w_h : water_height
    visited = [[0] * M for _ in '_' * N]
    for i in range(N):
        for j in range(M):
            if ground[i][j] < w_h and not visited[i][j]:
                q = [(i, j)]
                visited[i][j] = 1
                cnt = 1
                check = True
                while q:
                    vi, vj = q.pop(0)
                    for di, dj in delta:
                        ni, nj = vi + di, vj + dj
                        if 0 <= ni < N and 0 <= nj < M:
                            if ground[ni][nj] < w_h and not visited[ni][nj]:
                                visited[ni][nj] = 1
                                cnt += 1
                                q.append((ni, nj))
                        else:
                            check = False
                if check:
                    result += cnt
print(result)