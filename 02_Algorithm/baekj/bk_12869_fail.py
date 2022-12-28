# 뮤탈리스크 bfs
from itertools import permutations as pm
from collections import deque

targets = [[[0]]]
for i in range(2, 4):
    targets.append(list(pm(range(i), i)))


def bfs(hp):
    q = deque([(hp, 0)])
    while q:
        hp_v, cnt = q.popleft()

        lenV = len(hp_v)
        for target in targets[lenV - 1]:
            next_hp = []
            n = 2
            for i in target:
                scv = hp_v[i] - 3 ** n
                n -= 1
                if scv > 0:
                    next_hp.append(scv)

            if not next_hp:
                return cnt + 1

            if (next_hp, cnt+1) not in q:
                q.append((next_hp, cnt+1))


N = int(input())
HP = list(map(int, input().split()))
print(bfs(HP))

# # 뮤탈리스크 dfs
# from itertools import permutations as pm
#
# def dfs(hp, cnt):
#     global result
#
#     lenV = len(hp)
#     if not lenV:
#         result = min(result, cnt)
#         return
#     else:
#         pick = lenV
#
#     targets = list(pm(range(lenV), pick))
#     for target in targets:
#         next_hp = []
#         for n, i in enumerate(target):
#             scv = hp[i] - 3 ** (2 - n)
#             if scv > 0:
#                 next_hp.append(scv)
#         dfs(next_hp, cnt+1)
#
#
# N = int(input())
# HP = list(map(int, input().split()))
# result = 999999
# dfs(HP, 0)
# print(result)