# 부대 복귀

# 1
# n = 3
# roads = [[1, 2], [2, 3]]
# sources = [2, 3]
# destination = 1

# 2
n = 5
roads = [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]
sources = [1, 3, 5]
destination = 5


def solution(n, roads, sources, destination):
    def bfs(n, destination):
        visited = [INF] * (n + 1)
        visited[destination] = 0
        q = [destination]
        while q:
            v = q.pop(0)
            for w in adjL[v]:
                if visited[v] + 1 < visited[w]:
                    visited[w] = visited[v] + 1
                    q.append(w)
        return visited

    answer = []
    adjL = [[] for _ in range(n + 1)]
    for a, b in roads:
        adjL[a].append(b)  # 양방향
        adjL[b].append(a)  #

    INF = 1e5 + 1
    visited = bfs(n, destination)

    for source in sources:
        value = -1
        if visited[source] < INF:
            value = visited[source]
        answer.append(value)
    return answer

print(solution(n, roads, sources, destination))