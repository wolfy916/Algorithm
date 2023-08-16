# 용 조련사 룰루
import sys

def input():
    return sys.stdin.readline().rstrip('\n')

N, M = map(int, input().split())
P = list(map(int, input().split()))
dragons = []
for i in range(1, N + 1):
    dragons.append((P[i - 1], i))
dragons.sort()
temp = []
for order in [1, 3, 5, 2, 4]:
    print('---------------------')
    for idx in range(len(dragons)):
        if dragons[idx][1] == order:
            temp.append(dragons.pop(idx))
            break
    print(temp)
    differ = [0] * len(dragons)
    for i in range(1, len(dragons)):
        differ[i] = dragons[i][0] - dragons[i - 1][0]
    print(differ)
    for i in range(1, len(dragons)):
        differ[i] += differ[i-1]
    print(differ)
