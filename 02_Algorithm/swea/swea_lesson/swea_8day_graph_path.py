# stack 실습 그래프 경로

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    line = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    result = 0
    visited = [0 for _ in range(V+1)]
    STACK = [S]
    visited[S] = 1

    while len(STACK) != 0:

        for x in line:
            if x[0] == STACK[-1] and visited[x[1]] == 0:
                STACK.pop()
                num = x[1]
                visited[num] = 1
                break

        for x in line:
            if STACK[-1] == x[1] and visited[x[1]] == 1 and visited[x[0]] == 1:
                STACK.pop()
                num = x[0]
                break

        if num == G:
            result = 1
            break
        else:
            STACK += [num]

    print(f'#{tc} {result}')