# 상원이의 생일 파티

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj_Matrix = [[0]*(N+1) for _ in '_'*(N+1)]
    visited = [0]*(N+1)
    for _ in '_'*M:
        a, b = map(int, input().split())
        adj_Matrix[a][b] = 1
        adj_Matrix[b][a] = 1

    cnt = 0
    q = [1]
    visited[1] = 1
    while q:
        v = q.pop(0)
        if visited[v] > 3:
            break
        cnt += 1
        for w in range(1, N+1):
            if adj_Matrix[v][w] and not visited[w]:
                visited[w] = visited[v] + 1
                q.append(w)

    print(f'#{tc} {cnt-1}')
