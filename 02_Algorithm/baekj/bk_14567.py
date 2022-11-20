# 선수과목

N, M = map(int, input().split())
adjList = [[] for _ in '_'*(N+1)]
result = [0] * (N+1)
for _ in '_'*M:
    a, b = map(int, input().split())
    adjList[b].append(a)

q = []
for i in range(1, N+1):
    if not adjList[i]:
        result[i] = 1
        q.append(i)

while q:
    v = q.pop(0)
    for i in range(1, N+1):
        if v in adjList[i]:
            result[i] = result[v] + 1
            q.append(i)

# print(*adjList[1:])
print(*result[1:])

