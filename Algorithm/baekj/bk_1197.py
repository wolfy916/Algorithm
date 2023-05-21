# 최소 스패닝 트리 -> PRIM 방식 -> 메모리 초과
import sys
input = sys.stdin.readline


V, E = map(int, input().split())
adj_M = [[0]*(V+1) for _ in '_'*(V+1)]
for _ in '_'*E:
    a, b, c = map(int, input().split())
    adj_M[a][b] = c
    adj_M[b][a] = c

selected = [0] * (V+1)
MST = [1]
selected[1] = 1
result = 0
while selected.count(0) != 1:
    n_v = n_w = 0
    test = []
    for v in MST:
        for i in range(V+1):
            if adj_M[v][i] and not selected[i]:
                test.append([adj_M[v][i], v, i])
    test.sort()
    MST.append(test[0][2])
    selected[test[0][2]] = 1
    result += test[0][0]

print(result)