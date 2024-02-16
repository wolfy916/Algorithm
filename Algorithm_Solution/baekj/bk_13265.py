'''
색칠하기 - 백준 골드 5
분류 : dfs
'''
import sys

def input():
    return sys.stdin.readline().rstrip('\n')

def dfs(v, visited):
    global result
    if checked[v]: return
    checked[v] = True
    for w in adjL[v]:
        if not result: return
        if w in visited:
            if (len(visited) - visited.index(w)) % 2:
                result = False
                return
        else:
            dfs(w, visited + [w])

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        info = [tuple(map(int, input().split())) for _ in range(m)]

        adjL = [[] for _ in range(n + 1)]
        for a, b in info:
            if b in adjL[a]: continue
            adjL[a].append(b)
            adjL[b].append(a)

        result = True
        checked = [False] * (n + 1)
        for c in range(1, n + 1):
            if checked[c]: continue
            dfs(c, [c])
            if not result: break

        print("possible" if result else "impossible")