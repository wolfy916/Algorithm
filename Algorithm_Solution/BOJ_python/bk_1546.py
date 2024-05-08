N = int(input())
scores = list(map(int, input().split()))

M = max(scores)
sumV = 0
for i in range(N):
    sumV += scores[i] / M * 100

print(sumV/N)