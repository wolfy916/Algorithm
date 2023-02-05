# 맥주 마시면서 걸어가기

def dfs(x, y, ex, ey):
    if abs((x - ex) + (y - ey)) <= 1000:
        return True
    else:
        for i in range(n):
            if not visited[i]:
                distance = abs((x-stores[i][0]) + (y-stores[i][1]))
                if distance <= 1000:
                    visited[i] = 1
                    if dfs(stores[i][0], stores[i][1], ex, ey):
                        return True
                    else:
                        visited[i] = 0
    return False

for tc in range(int(input())):
    n = int(input())
    sx, sy = map(int, input().split())
    stores = [tuple(map(int, input().split())) for _ in '_'*n]
    ex, ey = map(int, input().split())
    visited = [0] * n
    if dfs(ex, ey, sx, sy):
        print('happy')
    else:
        print('sad')
