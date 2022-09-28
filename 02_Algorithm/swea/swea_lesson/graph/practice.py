# 상원이의 생일 파티 dfs stack 실패
def dfs(N):
    visited = [0] * (N + 1)
    stack = [0] * (N + 1)
    top = -1
    bottom = -1
    cnt = 0

    top += 1
    stack[top] = 1
    visited[1] = 1
    while top != bottom:
        v = stack[top]
        top += -1
        if visited[v] > 3:
            continue
        cnt += 1
        print(v)
        for w in adj_List[v]:
            if not visited[w]:
                visited[w] = visited[v] + 1
                top += 1
                stack[top] = w
    return cnt-1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj_List = [[] for _ in '_'*(N+1)]
    for _ in '_'*M:
        a, b = map(int, input().split())
        adj_List[a].append(b)
        adj_List[b].append(a)

    print(f'#{tc} {dfs(N)}')
