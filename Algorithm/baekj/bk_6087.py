# 레이저 통신

W, H = map(int, input().split())
area = [list(input()) for _ in '_'*H]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
minV = 10000
for i in range(H):
    for j in range(W):
        if area[i][j] == 'C':
            visited = [[minV] * W for _ in '_' * H]
            visited[i][j] = 0
            q = []
            for k in range(4):
                di, dj = delta[k]
                ni, nj = i + di, j + dj
                if 0 <= ni < H and 0 <= nj < W and area[ni][nj] != '*':
                    visited[ni][nj] = 0
                    q.append((ni, nj, k))
            while q:
                vi, vj, d = q.pop(0)
                if visited[vi][vj] > minV:
                    continue
                if area[vi][vj] == 'C' and (vi, vj) != (i, j):
                    minV = min(minV, visited[vi][vj])
                else:
                    for k in range(4):
                        di, dj = delta[k]
                        ni, nj = vi + di, vj + dj
                        # 유효성 검사 & 벽이 아님
                        if 0 <= ni < H and 0 <= nj < W and area[ni][nj] != '*' and visited[ni][nj] >= visited[vi][vj]:
                            if d == k:
                                visited[ni][nj] = min(visited[ni][nj], visited[vi][vj])
                            else:
                                visited[ni][nj] = min(visited[ni][nj], visited[vi][vj]+1)
                            
            print(minV)
            # for _ in range(H):
            #     print(*visited[_])
            exit()
            # direction[ni][nj] != k