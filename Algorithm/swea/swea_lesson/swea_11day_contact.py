def bfs(v): # v 시작 정점
    visited = [0]*101  # visited 생성
    q = []  # 큐 생성
    q.append(v)  # 시작점 인큐
    visited[v] = 1  # 시작점 처리 표시
    while q:  # 큐가 비어있지 않으면
        v = q.pop(0)  # 디큐
        for w in adjList[v]:  # 인접하고 미방문(인큐되지 않은) 정점 w가 있으면
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1

    max_v = max_idx = 0
    for j in range(101):
        if max_v <= visited[j]:
            max_v = visited[j]
            max_idx = j

    return max_idx


T = 10
for tc in range(1, T+1):
    N, start = map(int, input().split())
    contact = list(map(int, input().split()))

    adjList = [[] for _ in range(101)]
    for i in range(0, N-1, 2):
        adjList[contact[i]] += [contact[i+1]]

    print(f'#{tc} {bfs(start)}')
