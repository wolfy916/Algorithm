info1 = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges1 = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]

info2 = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
edges2 = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]


def promising(v):
    for i in range(1, N):
        for j in range(8):
            ni, nj = v_i+di[j]*i, v_j+dj[j]*i
            if 0 <= ni < N and 0 <= nj < N and chess[ni][nj] == 1:
                return False
    else:
        visited[v] = 1


def bfs(v):
    global cnt, lenV

    q = chd[0]
    q.sort(key=lambda x: info2[x])
    while q:

    if promising(v):
        if q == N:
            cnt += 1
        else:
            for i in range(N):
                bfs(v_i+1, i, q+1)
                bfs[v_i+1][i] = 0


answer = 1
wolf = 0

N = len(info2)
chd = [[] for _ in '_'*N]
par = [0]*N
for p, c in edges2:
    chd[p].append(c)
    par[c] = p
visited = [0]*N



