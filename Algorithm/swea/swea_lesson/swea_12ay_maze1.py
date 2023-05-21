def bfs(v):
    q = [v]  # 시작 정점의 인덱스가 담겨있는 큐 생성
    while q:  # 큐에 원소가 남아있다면
        v = q.pop(0)  # 디큐
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:  # 델타를 활용하여 상하좌우탐색
            ni = v[0] + di
            nj = v[1] + dj
            if 0 <= ni < 16 and 0 <= nj < 16 and maze[ni][nj] == 0:  # 유효 인덱스, 막힌 경로 검사
                maze[ni][nj] = 1             # 탐색의 기준이 된 원소값에서 1씩 더하여 할당
                q += [[ni, nj]]                                    # 갈 수 있는 경로들의 인덱스를 인큐
            elif 0 <= ni < 16 and 0 <= nj < 16 and maze[ni][nj] == 3:  # 도착점을 찾았다면 기준 원소값을 리턴
                return 1
    return 0


T = 10
for tc in range(1, T+1):
    test_case = int(input())
    maze = [list(map(int, input())) for _ in '_'*16]

    for i in range(16):  # start 인덱스 찾기
        for j in range(16):
            if maze[i][j] == 2:
                start = [i, j]

    print(f'#{tc} {bfs(start)}')