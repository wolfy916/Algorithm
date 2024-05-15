# 트리
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] dfs
def count(v):
    global answer
    if len(chd[v]) < 1:
        answer += 1
        return
    for w in chd[v]:
        count(w)

# [main]
if __name__ == '__main__':
    N = int(input())
    par = list(map(int, input().split()))
    d = int(input())

    chd = [[] for _ in range(N)]
    for i in range(N):
        if par[i] == -1 or i == d: continue
        chd[par[i]].append(i)

    answer = 0
    count(par.index(-1))
    print(answer if d != par.index(-1) else 0)