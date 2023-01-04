# 전력망을 둘로 나누기

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]

# n = 4
# wires = [[1,2],[2,3],[3,4]]

# n = 7
# wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]

# n은 2 이상 100 이하인 자연수
# wires는 길이가 n-1인 정수형 2차원 배열
def solution(n, wires):
    answer = 100
    adjL = [[] for _ in '_'*(n+1)]
    for v1, v2 in wires:
        adjL[v1].append(v2)
        adjL[v2].append(v1)

    def bfs(adjL, visited, n):
        q = [n]
        cnt = 1
        while q:
            v = q.pop(0)
            for w in adjL[v]:
                if not visited[w]:
                    cnt += 1
                    visited[w] = 1
                    q.append(w)
        return cnt

    for v1, v2 in wires:
        visited = [0]*(n+1)
        visited[v1] = 1
        visited[v2] = 1
        answer = min(answer, abs(n - 2 * bfs(adjL, visited, v1)))

    return answer

print(solution(n, wires))