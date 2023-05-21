# 중량제한
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(v, e, weigh):
    global S
    if v == e:
        return True
    else:
        for w, c in adjL[v]:
            if not visited[w] and weigh <= c:
                visited[w] = 1
                if dfs(w, e, weigh):
                    return True
        return False


N, M = map(int, input().split())  # 2 ≤ N ≤ 10,000, 1 ≤ M ≤ 100,000
adjL = [[] for _ in '_'*(N+1)]
for _ in '_'*M:
    A, B, C = map(int, input().split())  # 1 ≤ A, B ≤ N, 1 ≤ C ≤ 1,000,000,000
    adjL[A].append((B, C))
    adjL[B].append((A, C))
S, E = map(int, input().split())

left, right = 1, 1000000000
while left <= right:
    mid = (left + right)//2
    visited = [0] * (N + 1)
    visited[S] = 1
    if dfs(S, E, mid):
        left = mid + 1
    else:
        right = mid - 1

print(right)