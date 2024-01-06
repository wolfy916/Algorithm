'''
감시 - 백준 골드 4
분류 : 구현
'''
import sys

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 로직 함수
def solution(N, M, area):

    # [B-a] 감시할 수 있는 모든 경우의 수를 탐색하는 dfs 백트랙킹 함수
    def dfs(idx):
        nonlocal answer
        # [1] 모든 cctv의 감시 영역을 표시했다면 answer 갱신
        if idx >= len(cctvs):
            answer = min(answer, sum(map(lambda x: x.count(0), area)))
            return

        # [2] cctv를 회전시키며 탐색
        i, j = cctvs[idx]
        for k in range(4):
            used = []
            for dir in dirs[(i, j)]:
                d = (dir + k) % 4
                ni, nj = i + delta[d][0], j + delta[d][1]
                while 0 <= ni < N and 0 <= nj < M:
                    if area[ni][nj] == 6: break
                    if area[ni][nj] == 0:
                        area[ni][nj] = -1
                        used.append((ni, nj))
                    ni += delta[d][0]
                    nj += delta[d][1]
            dfs(idx + 1)  # 재귀
            for ui, uj in used:   # 백트랙킹
                area[ui][uj] = 0  #

    # [1] (key, value) = (cctv의 인덱스, 감시방향)의 형태로 저장
    delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
    cctv = [[], [0], [0, 2], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
    dirs = dict()
    for i in range(N):
        for j in range(M):
            if 0 < area[i][j] < 6:
                dirs[(i, j)] = cctv[area[i][j]]

    # [2] dfs 실행
    answer = N * M
    cctvs = list(dirs.keys())
    dfs(0)

    return answer


if __name__ == '__main__':
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]

    print(solution(N, M, area))