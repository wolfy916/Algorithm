# 개똥벌레

N, H = map(int, input().split())  # 2 ≤ N ≤ 200,000, 2 ≤ H ≤ 500,000
bottom = [0] * (H+1)  # ex) bottom[1] = 크기가 1인 석순의 갯수
top = [0] * (H+1)  # ex) top[2] = 크기가 2인 종유석의 갯수
for i in range(1, N+1):
    obstacle = int(input())
    # 홀수 -> 석순
    if i % 2:
        bottom[obstacle] += 1
    # 짝수 -> 종유석
    else:
        top[obstacle] += 1

print(bottom)
print(top)

for i in range(H-1, 0, -1):
    bottom[i] += bottom[i+1]
print(bottom)

for i in range(H-1, 0, -1):
    top[i] += top[i+1]
top = [0] + top[1:][::-1]
print(top)
paths = [bottom[i] + top[i] for i in range(1, H+1)]
print(paths)
minV = min(paths)
cntV = paths.count(minV)
print(minV, cntV)