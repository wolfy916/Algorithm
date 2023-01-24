# 등산 코스 정하기

# example 1
n = 7
paths = [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]
gates = [3, 7]
summits = [1, 5]
# [5, 3]

# example 2
# n = 7
# paths = [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]]
# gates = [1]
# summits = [2, 3, 4]
# [3, 4]

def solution(n, paths, gates, summits):
    adjM = [[0] * (n+1) for _ in '_' * (n+1)]
    for a, b, c in paths:
        adjM[a][b] = c
        adjM[b][a] = c
    minV = 10000001
    min_summit = 50001
    for gate in gates:
        for summit in summits:
            # print(f'{gate} -> {summit} ----------------------')
            visited = [0] * (n+1)
            visited[gate] = 1
            q = [(gate, 0)]
            while q:
                v, c = q.pop(0)
                # print(v, c)
                if v == summit:
                    if minV > c:
                        minV = c
                        min_summit = summit
                    elif minV == c:
                        min_summit = min(min_summit, summit)
                else:
                    for w in range(1, n+1):
                        if adjM[v][w] and not visited[w] and w not in gates and (w == summit or w not in summits):
                            visited[w] = 1
                            d = max(c, adjM[v][w])
                            q.append((w, d))
                            if w == summit:
                                visited[w] = 0
            # print(f'{min_summit} {minV} 여기가 현재 갱신된 값')
    answer = [min_summit, minV]
    return answer

print(solution(n, paths, gates, summits))