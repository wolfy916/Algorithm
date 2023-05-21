# 공주의 정원
from itertools import combinations as cb
import sys
input = sys.stdin.readline

def change(m, d):
    idx = d - 1
    for i in range(1, m):
        if i not in lst_30:
            if i == 2:
                idx += 28
                continue
            idx += 31
        else:
            idx += 30
    return idx

N = int(input())
lst_30 = [4, 6, 9, 11]

flower = []
for j in range(N):
    sm, sd, em, ed = map(int, input().split())
    if 11 < sm or em < 3:
        continue
    else:
        s_idx = change(sm, sd)
        e_idx = change(em, ed)
        flower.append((s_idx, e_idx))

# flower.sort(key=lambda x: x[2], reverse=True)
test_s, test_e = change(3, 1), change(11, 30)
for k in range(1, N+1):
    combs = list(cb(flower, k))
    for comb in combs:
        calendar = [0] * 365
        for s, e in comb:
            calendar[s] += 1
            calendar[e] += -1
        for i in range(1, len(calendar)):
            calendar[i] += calendar[i-1]
        for j in range(test_s, test_e+1):
            if not calendar[j]:
                break
        else:
            print(len(comb))
            sys.exit()
print(-1)