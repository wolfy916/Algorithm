# 탑

N = int(input())
a = list(map(int, input().split()))
cnt = [0]*N
top = []

for i in range(N):
    while top:
        if top[-1][1] > a[i]:
            cnt[i] = top[-1][0] + 1
            break
        top.pop()
    top.append([i, a[i]])
print(*cnt)