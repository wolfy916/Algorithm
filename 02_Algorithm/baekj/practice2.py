W, H = map(int, input().split())
area = [list(input()) for _ in '_'*H]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
minV = 10000
for i in range(H):
    for j in range(W):
        if area[i][j] == 'C':
            visited = [[minV] * W for _ in '_' * H]
            visited[i][j] = 1
            q = [(i, j, -1)]
            while q:
                vi, vj, d = q.pop(0)
                if visited[vi][vj] > minV:
                    continue
                if area[vi][vj] == 'C' and (vi, vj) != (i, j):
                    minV = min(minV, visited[vi][vj] - 1)
                else:
                    for k in range(4):
                        di, dj = delta[k]
                        ni, nj = vi + di, vj + dj
                        if 0 <= ni < H and 0 <= nj < W and area[ni][nj] != '*':
                            if not visited[ni][nj] or visited[ni][nj] > visited[vi][vj]:
                                if d == -1:
                                    visited[ni][nj] = visited[vi][vj]
                                else:
                                    if d == k:
                                        visited[ni][nj] = visited[vi][vj]
                                    else:
                                        visited[ni][nj] = visited[vi][vj] + 1
                                q.append((ni, nj, k))
            print(minV)
            for _ in range(H):
                print(*visited[_])
            exit()