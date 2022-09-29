# 13160. 5250. 최소 비용(제출용)
delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in '_'*N]

    visited = [[0]*N for _ in '_'*N]
    q = [(0, 0)]
    visited[0][0] = 1  # visit
    while q:
        vi, vj = q.pop(0)  # dequeue

        for di, dj in delta:
            ni, nj = vi + di, vj + dj
            if 0 <= ni < N and 0 <= nj < N:
                plus = area[ni][nj] - area[vi][vj]
                cost = visited[vi][vj] + 1
                if plus > 0:
                    cost += plus

                if not visited[ni][nj] or visited[ni][nj] > cost:
                    visited[ni][nj] = cost
                    q.append((ni, nj))

    print(f'#{tc} {visited[N-1][N-1] - 1}')



