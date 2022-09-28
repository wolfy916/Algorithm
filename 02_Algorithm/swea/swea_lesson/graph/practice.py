# 상원이의 생일 파티
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj_Area = [[0]*(N+1) for _ in '_'*(N+1)]
    visited = [0]*(N+1)
    for _ in '_'*M:
        a, b = map(int, input().split())
        adj_Area[a][b] = 1

    q = [1]
    visited[1] = 0
    while q:
        v = q.pop()
        for w in range(1, N+1):
            if adj_Area[v][w] == 1 and not visited[w]:
                visited[w] = visited[v] + 1
                q.append(w)

    result = 0
    for num in visited:
        if 0 < num < 3:
            result += 1

    print(f'#{tc} {result}')
