def bfs(v, e, n):  # v : 시작 노드, e : 도착 노드, n : 노드 수
    visited = [0] * (n+1)  # visited 생성
    q = [v]  # 시작 정점을 담고 있는 큐 생성
    visited[v] = 1  # 시작 정점 visited
    while q:  # 큐에 원소가 남아있다면 계속 진행
        v = q.pop(0)
        for w in adjList[v]:
            if w != e and visited[w] == 0:
                q += [w]
                visited[w] = visited[v] + 1
            elif w == e:
                return visited[v]
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())  # V : 노드 수, E : 간선 수

    adjList = [[] for _ in '_'*(V+1)]  # adjList 생성
    for _ in '_'*E:
        a, b = map(int, input().split())
        adjList[a] += [b]  # 쌍방향
        adjList[b] += [a]  #

    S, G = map(int, input().split())  # S : 출발 노드, G : 도착 노드

    print(f'#{tc} {bfs(S, G, V)}')