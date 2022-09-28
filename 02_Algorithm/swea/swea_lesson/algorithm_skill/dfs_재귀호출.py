def dfs(v):
    print(v)    #  v 방문
    visited[v] = 1
    for w in adjList[v]:
        if visited[w] == 0:     # 방문하지 않은 w
            dfs(w)

V, E = map(int, input().split())
N = V + 1
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

visited = [0] * N   # visited 생성
dfs(0)

'''
DFS알고리즘 - 재귀

DFS_Recursive(G, v)

    visited[v] = True  <- v 방문 설정
    
    for each all w in adjacency(G, v)
        if visited[w] != True
            DFS_Recursive(G, w)

'''