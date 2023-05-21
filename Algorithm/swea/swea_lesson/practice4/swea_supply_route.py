# 1249. 보급로
# 최소 가중치합 문제
# bfs 와 다이크스트라 풀이가 있음
# 이 문제의 경우 bfs가 압도적으로 빠름
# bfs 풀이

delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    area = [list(map(int, input())) for _ in '_' * N]

    visited = [[-1] * N for _ in '_' * N]
    q = [(0, 0)]
    visited[0][0] = area[0][0]  # visit
    while q:
        vi, vj = q.pop(0)  # dequeue
        for di, dj in delta:
            ni, nj = vi + di, vj + dj
            if 0 <= ni < N and 0 <= nj < N:
                cost = visited[vi][vj] + area[ni][nj]
                if visited[ni][nj] == -1 or visited[ni][nj] > cost:
                    visited[ni][nj] = cost
                    q.append((ni, nj))

    print(f'#{tc} {visited[N-1][N-1]}')

# # 다이크스트라 풀이
# delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#
#
# def dijkstra(a, b):
#     D[a][b] = 0
#     for _ in range(N*N):
#         vi = vj = 0
#         minV = INF
#         for i in range(N):
#             for j in range(N):
#                 if U[i][j] == 0 and minV > D[i][j]:
#                     vi, vj = i, j
#                     minV = D[i][j]
#
#         U[vi][vj] = 1
#         for di, dj in delta:
#             ni, nj = vi + di, vj + dj
#             if 0 <= ni < N and 0 <= nj < N:
#                 D[ni][nj] = min(D[ni][nj], D[vi][vj] + plan[ni][nj])
#
#         # for k in range(N):
#         #     print(*D[k])
#         # print('----------------------')
#
#     return D[N-1][N-1]
#
#
# INF = 90000
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     plan = [list(map(int, input()))for _ in '_'*N]
#     D = [[INF]*N for _ in '_'*N]
#     U = [[0]*N for _ in '_'*N]
#
#     print(f'#{tc} {dijkstra(0, 0)}')

