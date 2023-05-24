import sys
import heapq

INF = 10001
input = sys.stdin.readline
N, D = map(int, input().rstrip().split())

road = [[] * INF for _ in range(INF)]
heap = []
dist = [i for i in range(INF)]  # 지름길이 없을 경우 목적지 x 까지 주행하는 거리는 x 이다.

for _ in range(N):
    start, end, cost = map(int, input().rstrip().split())
    heapq.heappush(heap, (end, start, cost))  # 출발점으로부터 가까운 지름길순으로 저장하기 위해 (end, start, cost) 형태로 저장함

while heap:
    newEnd, newStart, newCost = heapq.heappop(heap)  # 출발점에 가장 가까운 end값을 갖는 지름길이 pop

    if newCost > (dist[newEnd] - dist[newStart]) or newEnd > D:  # 기존 값보다 비용이 크거나, 유효하지 않는 end값을 갖는 경우 continue
        continue

    distance = dist[newStart] + newCost

    if dist[newEnd] > distance:
        dist[newEnd] = distance

    for i in range(newEnd+1, INF):
        dist[i] = min(dist[i], dist[i-1]+1)

print(dist[D])