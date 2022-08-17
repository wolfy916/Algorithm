X = int(input())
N = int(input())
sumV = 0
for i in range(N):
    a, b = map(int, input().split())
    sumV += a * b
if X == sumV:
    print('Yes')
else:
    print('No')
