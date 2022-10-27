# 20퍼에서 시간초과 엔딩

from sys import stdin
from collections import deque

while True:
    w, h = map(int, stdin.readline().split())
    if w == h == 0:
        break

    room = [list(stdin.readline().strip()) for _ in range(h)]       # room 정보 받기

    # 로봇청소기의 출발 위치 찾기(인덱스 저장)
    # 더러운 곳의 개수 세기
    dirties = 0
    for i in range(h):
        for j in range(w):
            if room[i][j] == 'o':
                start = (i, j, 0)
            elif room[i][j] == '*':
                dirties += 1

    # 출발 지점에서 bfs로 출발하며 가장 먼저 찾는 곳이 가장 가까운 곳.
    # visited 처리를 하며 계속 찾아나가면 최단거리로 갈 수 있지 않을까

    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[0] * w for _ in range(h)]
    level = 1
    visited[start[0]][start[1]] = level
    cleared = deque()
    q = deque()
    q.append(start)
    ans = 0

    while q and dirties:
        # print(q)
        i, j, t = q.popleft()       # t = 이동한 거리
        for k in range(4):
            ni, nj = i + delta[k][0], j + delta[k][1]
            if 0 <= ni < h and 0 <= nj < w and room[ni][nj] != 'x' and visited[ni][nj] < level:
                if room[ni][nj] == '*' and (ni, nj) not in cleared:
                    dirties -= 1
                    cleared.append((ni, nj, t+1))

                    if dirties:     # 아직 치울 곳이 남아있는 경우
                        q.clear()
                        q.append((ni, nj, t+1))
                        level += 1
                        visited[ni][nj] = level
                        break
                    else:       # 마지막 청소를 끝낸 경우
                        ans = t + 1

                else:
                    q.append((ni, nj, t+1))
                    visited[ni][nj] = level

    if dirties > 0:
        print(-1)
    else:
        print(ans)