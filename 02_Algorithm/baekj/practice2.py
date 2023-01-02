# 여행 가자

N, M = int(input()), int(input())  # N <= 200, M <= 1000
adjM = [[0]*(N+1)]+[[0]+list(map(int, input().split())) for _ in '_'*N]
plans = list(map(int, input().split()))
visited = [0] * (N+1)
q = [plans[0]]
visited[plans[0]] = 1
while q:
    v = q.pop(0)
    for w in range(1, N+1):
        if adjM[v][w] and not visited[w]:
            visited[w] = 1
            q.append(w)
for city in plans:
    if not visited[city]:
        print("NO")
        exit()
print("YES")