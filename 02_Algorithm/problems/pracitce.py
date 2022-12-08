
def solution(n, s, a, b, fares):
    answer = 0
    adjM = [[0] * (n + 1) for _ in '_' * (n + 1)]
    for n1, n2, v in fares:
        adjM[n1][n2] = v
        adjM[n2][n1] = v

    def taxi_bfs(start, end, n):
        visited = [0] * (n+1)
        visited[start] = -1
        minV = 100000 * (n-1) + 1
        minV_path = []
        q = [(start, [start], 0)]
        while q:
            v, path, charge = q.pop(0)
            if v == end:
                if minV > charge:
                    minV = charge
                    minV_path = path
            else:
                for w in range(1, n+1):
                    w_charge = adjM[v][w]
                    if w_charge and (visited[w] == 0 or charge + w_charge <= visited[w]):
                        visited[w] = charge + w_charge
                        q.append((w, path+[w], visited[w]))
        return minV

    return taxi_bfs(s, a, n)

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
))