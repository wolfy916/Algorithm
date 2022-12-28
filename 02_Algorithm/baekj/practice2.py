# 어드벤처 게임
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(v, gold, n):
    global result
    if result == 'Yes':
        return

    if v == n:
        if maze[v][0] == 'T':
            if gold >= maze[v][1]:
                result = 'Yes'
                return
        else:
            result = 'Yes'
            return
    else:
        if maze[v][0] == 'L':
            gold = max(gold, maze[v][1])

        elif maze[v][0] == 'T':
            if gold >= maze[v][1]:
                gold -= maze[v][1]

        for w in maze[v][2:]:
            if w:
                if not visited[w] or visited[w] < gold:
                    visited[w] = gold
                    dfs(w, gold, n)


while True:
    n = int(input())
    if not n:
        break
    maze = [[0]]
    for _ in '_'*n:
        char, *info = input().split()
        maze.append([char]+list(map(int, info)))
    visited = [0] * (n + 1)
    result = 'No'
    dfs(1, 0, n)
    print(result)