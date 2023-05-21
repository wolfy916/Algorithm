# 별자리 만들기
def distance(ax, ay, bx, by):
    return ((ax-bx)**2 + (ay-by)**2) ** 0.5

def prim(s):
    visited = set()  # visited: 현재까지 방문한 정점들의 집합
    visited.add(s)
    result = 0
    INF = 1500 * (n-1)

    # MST 에서는 노드 개수 n 개일 때, 선택해야할 간선수는 n-1 개
    # n-1 개의 간선을 선택할 때까지 반복
    for _ in '_' * (n-1):
        # min_d: 현재 방문한 정점에서 갈 수 있는 간선의 최소 비용
        # next_n: 현재 방문한 노드에서 최소 비용으로 갈 수 있는 노드
        min_d, next_n = INF, -1

        # 현재까지 방문한 모든 노드에 대하여
        for node in visited:
            for j in range(n):
                # 연결되어 있고 아직 방문하지 않은 모든 노드 중
                if j not in visited:
                    # 비용이 가장 작은 노드를 찾는다.
                    if 0 < adjM[node][j] < min_d:
                        min_d = adjM[node][j]
                        next_n = j

        result += min_d
        visited.add(next_n)

    return result


n = int(input())  # 1 ≤ n ≤ 100
stars = []
for _ in '_'*n:
    str_x, str_y = input().split()
    x, y = float(str_x), float(str_y)
    stars.append((x, y))

# 별 사이의 거리 비용(가중치)을 adjM에 표기
adjM = [[0]*n for _ in '_'*n]
for i in range(n-1):
    for j in range(i+1, n):
        if i != j:
            ax, ay = stars[i]
            bx, by = stars[j]
            d = round(distance(ax, ay, bx, by), 3)
            adjM[i][j] = d  # 무방향 가중치
            adjM[j][i] = d  #

print(round(prim(0), 2))