# 피리 부는 사나이

N, M = map(int, input().split())
area = [list(input()) for _ in '_'*N]
direction = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
visited = [[0]*M for _ in '_'*N]
g_num = 1
for i in range(N):
    for j in range(M):
        # 한번도 방문하지 않은 곳에서 출발
        if not visited[i][j]:
            path = [(i, j)]  # 출발부터 경로에 담음
            stack = [(i, j)]  # dfs를 돌릴거임
            visited[i][j] = g_num  # 1
            while stack:
                vi, vj = stack.pop()
                di, dj = direction[area[vi][vj]]
                ni, nj = vi+di, vj+dj
                # 한번도 방문하지 않은 곳이라면
                if not visited[ni][nj]:
                    visited[ni][nj] = g_num  # 같은 그룹이되는곳임
                    stack.append((ni, nj))
                    path.append((ni, nj))
                # 다른 그룹이라면
                elif visited[ni][nj] != g_num:
                    for wi, wj in path:
                        visited[wi][wj] = visited[ni][nj]
                    break  # 그룹 합류 시키고 while문 강제종료 -> g_num 늘어나지 않음
            else:
                g_num += 1
# for _ in range(N):
#     print(*visited[_])
print(g_num - 1)