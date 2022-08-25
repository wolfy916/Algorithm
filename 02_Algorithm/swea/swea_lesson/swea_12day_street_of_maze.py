# 미로의 거리
def bfs(v, n):
    q = [v]  # 시작 정점의 인덱스가 담겨있는 큐 생성
    while q:  # 큐에 원소가 남아있다면
        v = q.pop(0)  # 디큐
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:  # 델타를 활용하여 상하좌우탐색
            ni = v[0] + di
            nj = v[1] + dj
            if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] == 0:  # 유효 인덱스, 막힌 경로 검사
                maze[ni][nj] = maze[v[0]][v[1]] + 1                # 탐색의 기준이 된 원소값에서 1씩 더하여 할당
                q += [[ni, nj]]                                    # 갈 수 있는 경로들의 인덱스를 인큐
            elif 0 <= ni < N and 0 <= nj < N and maze[ni][nj] == -1:  # 도착점을 찾았다면 기준 원소값을 리턴
                return maze[v[0]][v[1]]
    return 2  # while문을 다 돌았다면 도착점에 도달하지 못했으므로 2 리턴


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # N x N 정방행렬 미로
    maze = [list(map(int, input())) for _ in '_'*N]

    for i in range(N):  # start 인덱스 찾기, 도착 정점의 원소 -1로 교체
        for j in range(N):
            if maze[i][j] == 2:
                start = [i, j]
            if maze[i][j] == 3:
                maze[i][j] = -1

    print(f'#{tc} {bfs(start, N) - 2}')  # 시작점의 원소 2부터 카운팅이 되기 때문에 2를 빼고 출력

