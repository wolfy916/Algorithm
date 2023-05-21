# 10019. 5251. 최소 이동 거리(제출용)
# dfs - stack - index 풀이

T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())

    V = N + 1
    adj_M = [[0] * V for _ in '_' * V]
    for _ in '_' * E:
        s, e, adj_M[s][e] = map(int, input().split())

    # visited, stack 생성, 초기값이 0이라 따로 넣을 필요 없음
    visited = [0] * V
    stack = [0] * E
    top = 0

    # stack이 비어있을 때까지
    while top > -1:

        # pop
        v = stack[top]
        top -= 1

        for w in range(V):
            if adj_M[v][w]:  # 간선이 있는지 확인
                distance = visited[v] + adj_M[v][w]  # 거리를 합산해가며 visited에 할당
                if not visited[w] or visited[w] > distance:  # 방문하지 않은 곳 혹은 방문했지만 이동거리가 더 적게 나온 경우
                    visited[w] = distance  # visited 이동거리값 갱신
                    # push
                    top += 1
                    stack[top] = w

    print(f'#{tc} {visited[N]}')