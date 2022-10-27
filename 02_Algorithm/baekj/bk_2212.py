# 센서

N = int(input())
K = int(input())
sensors = list(map(int, input().split()))
sensors.sort()
distance = []
for i in range(N-1):
    distance.append(sensors[i+1] - sensors[i])
distance.sort(reverse=True)
print(sum(distance[K-1:]))