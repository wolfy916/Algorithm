# 덩치

N = int(input())
people = [list(map(int, input().split())) for _ in '_'*N];
ranking = [1] * N
for i in range(N-1):
    xi, yi = people[i]
    for j in range(i+1, N):
        xj, yj = people[j]
        if xi > xj and yi > yj:
            ranking[j] += 1
        elif xi < xj and yi < yj:
            ranking[i] += 1
print(*ranking)