def bfs(N):
    cnt = 0
    front = -1
    rear = -1
    q = [0] * (N + 1)
    rear += 1
    q[rear] = 1  # 출발노드 1
    visited = [0] * (N + 1)
    visited[1] = 1
    while front != rear:
        front += 1
        v = q[front]
        if visited[v] > 3:
            break
        cnt += 1
        # for w in range(1, N+1):
        #    if adj[v][w] and visited[w]==0:
        for w in adjL[v]:
            if visited[w] == 0:
                rear += 1
                q[rear] = w
                visited[w] = visited[v] + 1
    return cnt - 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    adjM = [[0] * (N + 1) for _ in range(N + 1)]
    adjL = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        adjM[a][b] = 1
        adjM[b][a] = 1
        adjL[a].append(b)
        adjL[b].append(a)

    print(f'#{tc} {bfs(N)}')