# 공주님을 구해라!
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs():
    result1 = 10001  # 아이템 따위 안먹고 가는 용사
    result2 = 10001  # 템빨 용사
    INF = 10000
    visited = [[INF]*(M+2) for _ in '_'*(N+2)]  # INF값 도배
    q = [[1, 1]]
    visited[1][1] = 0  # 첫 칸은 걸린 시간 0
    while q:
        vi, vj = q.pop(0)

        # 빈 손으로 공주를 만남
        if vi == N and vj == M:
            result1 = visited[vi][vj]

        # 전설의 그람을 발견 !
        elif area[vi][vj] == 2:
            result2 = visited[vi][vj] + abs(vi-N) + abs(vj-M)

        # 공주 미발견
        else:
            for di, dj in delta:
                ni, nj = vi+di, vj+dj
                # 벽이 아니고, visited에 기록된 단위시간 값이 더 작다면 visited 갱신 및 append
                if area[ni][nj] != 1 and visited[ni][nj] > visited[vi][vj] + 1:
                    visited[ni][nj] = visited[vi][vj] + 1
                    q.append([ni, nj])

    # 더 작은 값을 return
    return min(result1, result2)

N, M, T = map(int, input().split())  # 3 ≤ N, M ≤ 100, 1 ≤ T ≤ 10000
area = [[1]*(M+2)]+[[1] + list(map(int, input().split())) + [1] for _ in '_'*N] + [[1]*(M+2)]

result = bfs()  # 상남자는 특, 인자 전달 같은거 안함
if result <= T:
    print(result)
else:
    print('Fail')
