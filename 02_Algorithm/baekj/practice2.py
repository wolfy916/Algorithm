# 별자리 만들기
N = int(input())
stars = []
for _ in range(N):
    stars.append(list(map(float, input().split())))
# print(stars)

def getDistance(i,j, ei,ej):
    a = abs(i-ei)**2
    b = abs(j-ej)**2
    c = (a+b)**(0.5)
    return c

INF = 1000000
mst = [INF]*N
mst[0] = 0
visited = [0]*N
ei,ej = stars[0]
for _ in range(N-1):
    minV = INF
    u = 0                 # 이번에 최소경로 출발지
    for star in range(N):
        if not visited[star]:
            i,j = stars[star]
            distance = getDistance(i,j,ei,ej)
            if distance < minV :
                minV = distance
                u = star
    visited[u] = 1
    ei,ej = stars[u]

    for s in range(N):
        if s!=u and not visited[s]: # s가 자기자신이 아니면서 아직 mst안 정해진 별일떄
            i,j = stars[s]
            mst[s] = min(mst[s], getDistance(i,j,ei,ej))
            print(u,s,mst[s])
print(mst)
print(round(sum(mst), 2))