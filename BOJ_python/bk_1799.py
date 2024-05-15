# 비숍
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [1] 데이터 입력
N = int(input())
board = [list(input().split()) for _ in range(N)]

# [2] nodeinfo: 해당 좌표가 속한 우상향 대각선 번호를 저장
#     possible: 기본적으로 체스를 둘 수 있는 곳의 좌표를 저장하지만 아래와 같이 분류
#               (1) 체스판의 흑, 백 칸을 나누어 분류
#               (2) 해당 좌표가 속한 좌상향 대각선 번호로 분류
#               위 분류 조건은 백트랙킹의 부하를 줄이기 위함임.
nodeinfo = dict()
possible = [[[] for _ in range(2 * N)] for _ in range(2)]
for i in range(N):
    for j in range(N):
        if board[i][j] == '1':
            line1 = N - i + j
            line2 = i + j + 1
            possible[line2 % 2][line1].append((i, j))
            nodeinfo[(i, j)] = line2

# [B] dfs + 백트랙킹
def dfs(n, v, c):  # n: 좌상향 대각선 번호, v: 현재까지 놓은 비숍의 개수, c: 흑, 백
    # [B-1] 매 탐색시 정답 갱신
    answer[c] = max(answer[c], v)
    # [B-2] 마지막 좌상향 대각선까지만 탐색하고 return
    if n > 2 * N - 1:
        return
    # [B-3] 우상향 대각선 번호를 visited로 활용
    for vi, vj in possible[c][n]:
        if used[nodeinfo[(vi, vj)]]: continue
        used[nodeinfo[(vi, vj)]] = True
        dfs(n+1, v+1, c)
        # [B-4] 백트랙킹
        used[nodeinfo[(vi, vj)]] = False
    # [B-5] n번째 좌상향 대각선 위에 비숍을 둘 곳이 있을 수 있지만,
    #       없을 수도 있기 때문에 다음 n+1로 재귀하는 장치를 마련
    dfs(n+1, v, c)

# [3] 출력부
answer = [0, 0]  # 흑, 백
used = [False] * (2 * N)  # 우상향 대각선을 기준으로 기록
for i in range(2):  # 흑, 백으로 2번 함수 실행
    dfs(0, 0, i)
print(sum(answer))