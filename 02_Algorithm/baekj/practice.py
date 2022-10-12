# 원 이동하기 1
from sys import stdin
input = stdin.readline


# 재귀
def dfs(v, cnt):
    global maxV
    visited[v] = 1
    if len(adjL[v]) == 1:
        if maxV < cnt:
            maxV = cnt
    for w in adjL[v]:
        if not visited[w]:
            dfs(w, cnt+1)

# 스택
# def dfs(k, cnt):
#     global maxV
#     visited[k] = 1
#     stack = [(k, cnt)]
#     while stack:
#         v, cnt = stack.pop()
#         if len(adjL[v]) == 1:
#             if maxV < cnt:
#                 maxV = cnt
#         for w in adjL[v]:
#             if not visited[w]:
#                 visited[w] = 1
#                 stack.append((w, cnt+1))


N = int(input())
circles = [list(map(int, input().split())) + [x] for x in range(1, N+1)]

circles = [0] + sorted(circles, key=lambda x: x[2])
par = [0] * (N+1)
adjL = [[] for _ in '_'*(N+1)]

end_node = []
for i in range(1, N+1):
    x, y, r, num1 = circles[i]
    for j in range(i+1, N+1):
        cx, cy, cr, num2 = circles[j]
        d = (cx-x)**2 + (cy-y)**2
        if d < (cr-r)**2 or d == 0:
            adjL[num1].append(num2)
            adjL[num2].append(num1)
            par[num1] = num2
            break

    if not par[num1]:
        adjL[num1].append(0)
        adjL[0].append(num1)

    if len(adjL[num1]) == 1:
        end_node.append(num1)

maxV = 0
for s in end_node:
    visited = [0] * (N+1)
    dfs(s, 0)

print(maxV)

