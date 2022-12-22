# 1번 입력
n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
# result = 82


def solution(n, s, a, b, fares):

    def dijkstra(n, s, dout, INF):
        d = dout[:]
        d[s] = 0
        for i in range(1, n+1):
            d[i] = adjM[s][i]
        U = [s]
        for _ in range(n-1):
            w = 0
            for i in range(1, n+1):
                if i not in U and d[i] < d[w]:
                    w = i
            U.append(w)
            for v in range(1, n+1):
                if 0 < adjM[w][v] < INF:
                    d[v] = min(d[v], d[w] + adjM[w][v])
        return d

    INF = 10000000
    adjM = [[INF] * (n + 1) for _ in '_' * (n + 1)]
    for n1, n2, v in fares:
        adjM[n1][n2] = v
        adjM[n2][n1] = v
    for i in range(1, n+1):
        adjM[i][i] = 0

    together = dijkstra(n, s, adjM[s], INF)
    a_charge = dijkstra(n, a, adjM[a], INF)
    b_charge = dijkstra(n, b, adjM[b], INF)

    answer = INF
    for i in range(1, n+1):
        answer = min(answer, together[i]+a_charge[i]+b_charge[i])
    return answer

print(solution(n, s, a, b, fares))