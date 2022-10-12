from sys import stdin
from collections import deque
input = stdin.readline

# bfs
def bfs(n):
    INF = 101
    visited = [INF] * 101  # visited를 INF값으로 설정
    q = deque([(n, 0)])
    while q:
        v, v_cnt = q.popleft()
        if v == 100:       # 100번 칸에 도착하면 cnt값 return
            return v_cnt
        else:
            w_cnt = v_cnt + 1
            for i in range(1, 7):  # 주사위 굴리기
                w = v + i
                # 유효 인덱스 검사 + 방문한 곳의 주사위 던진 횟수가 w_cnt보다 작다면 가지치기
                if 0 <= w < 101 and visited[w] >= w_cnt:
                    visited[w] = w_cnt
                    q.append((board[w], w_cnt))


N, M = map(int, input().split())
board = list(range(101))  # board = [0, 1, 2, ...., 100]
for _ in '_'*N:
    x, y = map(int, input().split())
    board[x] = y  # board에 사다리 추가
for _ in '_'*M:
    u, v = map(int, input().split())
    board[u] = v  # board에 뱀 추가
print(bfs(1))