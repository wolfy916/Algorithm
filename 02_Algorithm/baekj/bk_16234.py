# 인구 이동

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def dfs(i, j):
    global cntV, sumV
    for di, dj in delta:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < N:
            if not visited[ni][nj] and L <= abs(land[i][j] - land[ni][nj]) <= R:
                visited[ni][nj] = 1
                union.append((ni, nj))  # 연합에 속한 국가 인덱스
                cntV += 1               # 연합 국가 수
                sumV += land[ni][nj]    # 연합 총 인구수
                dfs(ni, nj)

N, L, R = map(int, input().split())
land = [list(map(int, input().split())) for _ in '_'*N]

day = 0
while True:
    unions = []
    cnt_of_unions = [0] * (N**2)
    total_of_unions = [0] * (N**2)
    visited = [[0]*N for _ in '_'*N]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                union = [(i, j)]
                cntV = 1
                sumV = land[i][j]
                dfs(i, j)
                cnt_of_unions[len(unions)] = cntV
                total_of_unions[len(unions)] = sumV
                unions.append(union)

    for k, union in enumerate(unions):
        temp = total_of_unions[k] // cnt_of_unions[k]  # 연합 총 인구수 / 연합 국가수
        for i, j in union:
            land[i][j] = temp  # 인구 갱신

    if len(unions) == N**2:
        print(day)
        break

    day += 1