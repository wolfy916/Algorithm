# 탈출
R, C = map(int, input().split())
forest = [list(input()) for _ in '_' * R]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = []
for i in range(R):
    for j in range(C):
        if forest[i][j] == '*':
            q.append((i, j))  # 물 위치
        elif forest[i][j] == 'S':
            S = (i, j)  # 고슴도치 위치
            forest[i][j] = '.'
        elif forest[i][j] == 'D':
            D = (i, j)  # 비버 굴 위치

q = [S] + q  # 고슴도치가 q의 첫번째 원소로 오도록
visited = [[0] * C for _ in '_' * R]
visited[S[0]][S[1]] = 1
while q:
    vi, vj = q.pop(0)
    for di, dj in delta:
        ni, nj = vi + di, vj + dj
        if 0 <= ni < R and 0 <= nj < C:
            # 이동할 곳이 땅이면
            if forest[ni][nj] == '.':
                # 현재 위치도 물이면
                if forest[vi][vj] == '*':
                    forest[ni][nj] = '*'
                    q.append((ni, nj))
                # 현재 위치가 물이 아니면서 방문하지 않은 곳이면
                elif not visited[ni][nj]:
                    visited[ni][nj] = visited[vi][vj] + 1  # cnt
                    q.append((ni, nj))
            # 현재 위치가 침수되지 않고, 이동할 곳이 비버굴이라면
            elif forest[vi][vj] != '*' and (ni, nj) == D:
                print(visited[vi][vj])
                exit()
print('KAKTUS')