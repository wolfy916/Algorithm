def fishing(g, p, v, c, N):  # g : 게이트 번호, p : 사람 수 , v : visited, c : 0 -> 사람수가 홀수, 1 -> 사람수가 짝수




def bfs(N):
    global order
    visited = [0]*(N+1)  # visited 생성
    q = []  # 큐 생성
    if order[0][1] % 2:  # 시작점 인큐
        couple = order[0] + [0]
        q += [couple]
    else:
        left = order[0] + [1]
        right = order[0] + [2]
        q += [left]
        q += [right]

    i = 0
    while i != 3:
        v = q.pop(0)  # 디큐
        if v[2] == 0:
            q += [fishing(v[0], v[1], visited, v[2], N)]
        else:
            q += [fishing(v[0], v[1], visited, v[2], N)]  # left
            v = q.pop(0)
            q += [fishing(v[0], v[1], visited, v[2], N)]  # right
        i += 1

    return


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    point = [list(map(int, input().split())) for _ in '_'*3]

    minV = 100000
    for i in range(3):
        for j in range(3):
            for k in range(3):
                sumV = 0
                if i != j and j != k and i != k:
                    order = [point[i], point[j], point[k]]
                    bfs(N)
                if minV > sumV:
                    minV = sumV

    print(f'#{tc} {minV}')

