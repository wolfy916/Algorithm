# DFS와 BFS

def dfs(v):  # 재귀를 이용하여 구현한 dfs
    global path_dfs, adjList  # 전역변수 가져오기

    if visited_dfs[v] == 1:  # 방문했으면
        return  # 그냥 돌아오기

    visited_dfs[v] = 1  # visited
    if v not in path_dfs:  # 최종 출력할 경로 리스트에 v가 없으면 추가
        path_dfs += [v]

    adjList[v].sort()  # 문제에서 작은 수부터 우선탐색이므로
    for x in adjList[v]:  # 갈 수 있는 모든 경로에 대하여 재귀호출
        dfs(x)
    return path_dfs


def bfs(v, N):  # 큐를 이용하여 bfs 구현
    visited = [0]*(N+1)  # visited 생성
    q = []  # 큐 생성
    q += [v]  # 시작점 인큐
    visited[v] = 1  # visited
    path = []  # 최종 출력할 경로 리스트 생성
    while q:  # 큐의 원소가 존재하면
        v = q.pop(0)  # 디큐
        path += [v]  # 경로에 추가
        adjList[v].sort()  # 문제가 작은 번호 우선탐색이므로
        for w in adjList[v]:  # w : v에서 갈 수 있는 정점
            if visited[w] == 0:  # 방문하지 않았다면
                q += [w]  # 인큐
                visited[w] = 1  # visited
    return path


N, M, V = map(int, input().split())  # N : 정점 수, M : 간선 수, V : 시작 정점
adjList = [[] for _ in range(N+1)]  # adjList : 간선을 받을 2차원 리스트
for _ in range(M):
    a, b = map(int, input().split())
    adjList[a] += [b]  # 쌍방향 노드
    adjList[b] += [a]  #

visited_dfs = [0] * (N + 1)
path_dfs = []  # 탐색 경로를 담을 리스트
print(*dfs(V))
print(*bfs(V, N))