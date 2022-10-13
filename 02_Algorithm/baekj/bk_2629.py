# 양팔 저울
from sys import stdin
input = stdin.readline

input()  # 1 <= 추의 개수 <= 30
weights = list(map(int, input().split()))  # 1g <= 추의 무게 <= 500g
input()  # 1 <= 구슬의 개수 <= 7
beads = list(map(int, input().split()))  # 1g <= 구슬의 무게 <= 40,000g

results = [weights.pop(0)]
while weights:
    test = weights.pop(0)
    add_lst = [test]
    for result in results:
        sumV = test + result
        if sumV not in results:
            add_lst.append(sumV)
        diffV = abs(test - result)
        if diffV not in results:
            add_lst.append(diffV)
    results += add_lst

for bead in beads:
    if bead in results:
        print('Y', end=' ')
    else:
        print('N', end=' ')