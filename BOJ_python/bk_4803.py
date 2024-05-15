# 트리
import sys
from collections import deque as dq

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [main]
if __name__ == '__main__':
    tc = 1
    while True:
        n, m = map(int, input().split())
        if (n, m) == (0, 0): break
        edges = [tuple(map(int, input().split())) for _ in range(m)]
        adjL = [[] for _ in range(n + 1)]
        for a, b in edges:
            adjL[a].append(b)  # 양방향 간선 기록
            adjL[b].append(a)  #

        visited = [False] * (n + 1)
        answer = 0
        for i in range(1, n + 1):
            if visited[i]: continue
            q = dq([i])
            visited[i] = True
            flag = True
            while q and flag:
                v = q.popleft()
                for w in adjL[v]:
                    if visited[w]:
                        flag = False
                        break
                    visited[w] = True
                    adjL[w].remove(v)  # 부모 노드로 되돌아갈 간선 자르기
                    q.append(w)
            if flag: answer += 1

        if answer == 0:
            print(f'Case {tc}: No trees.')
        elif answer == 1:
            print(f'Case {tc}: There is one tree.')
        else:
            print(f'Case {tc}: A forest of {answer} trees.')

        tc += 1