from collections import deque
from copy import deepcopy


def spin(x, y, r):
    new_graph = deepcopy(graph)
    nex, ney = 0, 0
    for i in range(r):
        for j in range(r):
            new_graph[x + j][y + r - i - 1] = graph[x + i][y + j] if graph[x + i][y + j] <= 0 else graph[x + i][
                                                                                                       y + j] - 1
            if graph[x + i][y + j] == -1:
                nex, ney = x + j, y + r - i - 1
            elif graph[x + i][y + j] == -2:
                p = people[(x + i, y + j)]
                del people[(x + i, y + j)]
                people[(x + j, y + r - i - 1)] = p

    return new_graph, nex, ney


# 캐릭터 움직이기
def move(x, y, ex, ey, p):
    global answer
    canMove = 0
    dis = abs(ex - x) + abs(ey - y)
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 > nx or 0 > ny or N <= nx or N <= ny: continue
        if graph[nx][ny] > 0: continue
        if dis > abs(ex - nx) + abs(ey - ny):
            canMove = (nx, ny)
            answer += p
            break
    if not canMove:
        return (x, y)
    else:
        return canMove


def findSquare(ex, ey):
    r = 2
    flag = 0
    find = []
    while True:
        queue = deque([(ex, ey)])
        visited = [[False] * (N) for _ in range(N)]
        visited[ex][ey] = True
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 > nx or 0 > ny or N <= nx or N <= ny: continue
                if abs(nx - ex) >= r or abs(ny - ey) >= r: continue
                if visited[nx][ny]: continue
                if graph[nx][ny] == -2:
                    flag = 1
                    find.append((nx, ny))
                visited[nx][ny] = True
                queue.append((nx, ny))
        if not flag:
            r += 1
        else:
            break

    return find, r


N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

people = dict()
for _ in range(M):
    x, y = map(lambda x: int(x) - 1, input().split())
    graph[x][y] = -2
    people[(x, y)] = people.get((x, y), 0) + 1
# 출구 좌표
ex, ey = map(lambda x: int(x) - 1, input().split())
graph[ex][ey] = -1

answer = 0
for k in range(K):
    Move = dict()
    for (x, y), p in people.items():
        nx, ny = move(x, y, ex, ey, p)
        graph[x][y] = 0
        if nx == ex and ny == ey:
            continue
        Move[(nx, ny)] = Move.get((nx, ny), 0) + p
    people = Move
    for (x, y) in people.keys():
        graph[x][y] = -2

    if not people:
        break
    finded, r = findSquare(ex, ey)
    finded.sort()
    s_x, s_y = finded[0]
    if ex > s_x:
        s_startx = ex - (r - 1) if ex - (r - 1) >= 0 else 0
    else:
        s_startx = s_x - (r - 1) if s_x - (r - 1) >= 0 else 0
    if ey > s_y:
        s_starty = ey - (r - 1) if ey - (r - 1) >= 0 else 0
    else:
        s_starty = s_y - (r - 1) if s_y - (r - 1) >= 0 else 0
    graph, ex, ey = spin(s_startx, s_starty, r)

print(answer)
print(ex + 1, ey + 1)