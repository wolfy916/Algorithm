# 구간 합 구하기 4

N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))
maxV = 0
line = []
for _ in '_'*M:
    i, j = map(int, input().split())
    line.append((i, j))
    maxV = max(maxV, i, j)
for k in range(1, maxV+1):
    nums[k] += nums[k-1]
for i, j in line:
    print(nums[j]-nums[i-1])