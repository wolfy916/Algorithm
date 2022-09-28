# 상원이의 생일 파티
def dfs(i, N, c):
    stack = [0]*(N + 1)
    top = 0
    bottom = -1
    stack[top] = i
    visited[top] = 1
    while top != bottom:
        v = stack[top]
        top += -1
        if visited[v] > 3:
            continue
        c += 1
        for w in adj_List[v]:
            if not visited[w]:
                visited[w] = visited[v] + 1
                top += 1
                stack[top] = w
    return c-1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj_List = [[] for _ in '_'*(N+1)]
    for _ in '_'*M:
        a, b = map(int, input().split())
        adj_List[a].append(b)

    result = cnt = 0
    visited = [0] * (N + 1)

    print(f'#{tc} {dfs(1, N, 0)}')
