from collections import deque as dq

# [A] 카드의 좌표를 원소로 갖는 리스트를 리턴하는 함수
def search_card(board, N, M):
    cards = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0: continue
            cards.append((i, j))
    return cards

# [B] S 지점에서 E 지점으로 이동하는 최소비용을 리턴하는 함수
def bfs(board, N, M, si, sj, ei, ej, log):
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = dq([(si, sj)])
    visited = [[100] * M for _ in range(N)]
    visited[si][sj] = 0
    found_cards = []
    found_cards_cnt = []
    while q:
        vi, vj = q.popleft()
        if len(log) % 2:
            if (vi, vj) == (ei, ej): return visited[vi][vj] + 1
        else:
            if board[vi][vj] and (vi, vj) not in log:
                for f_card in found_cards:
                    i, j = f_card
                    if board[vi][vj] == board[i][j]:
                        break
                else:
                    found_cards.append((vi, vj))
                    found_cards_cnt.append(visited[vi][vj] + 1)
        for di, dj in delta:
            ni, nj = vi + di, vj + dj
            if ni < 0 or nj < 0 or ni >= N or nj >= M: continue
            if visited[vi][vj] + 1 < visited[ni][nj]:
                visited[ni][nj] = visited[vi][vj] + 1
                q.append((ni, nj))
            ti, tj = ni, nj
            while True:
                if ni < 0 or nj < 0 or ni >= N or nj >= M:
                    ni -= di; nj -= dj;
                    break
                if board[ni][nj] and (ni, nj) not in log: break
                ni += di; nj += dj;
            if (ti, tj) == (ni, nj): continue
            if visited[vi][vj] + 1 < visited[ni][nj]:
                visited[ni][nj] = visited[vi][vj] + 1
                q.append((ni, nj))
    return found_cards, found_cards_cnt

# [C] dfs 탐색 함수
def dfs(board, vi, vj, N, M, cards, log, cnt):
    global answer
    if cnt > answer: return
    if len(cards) == len(log):
        answer = min(answer, cnt)
        return
    if len(log) % 2:
        for ei, ej in cards:
            if (vi, vj) == (ei, ej): continue
            if board[vi][vj] == board[ei][ej]:
                break
        add = bfs(board, N, M, vi, vj, ei, ej, log)
        dfs(
            board, ei, ej, N, M,
            cards, log + [(ei, ej)],
            cnt + add
        )
    else:
        f_cards, f_cards_cnt = bfs(board, N, M, vi, vj, 0, 0, log)
        for card, add in zip(f_cards, f_cards_cnt):
            si, sj = card
            dfs(
                board, si, sj, N, M,
                cards, log + [(si, sj)],
                cnt + add
            )

# [D] 메인 함수
def solution(board, r, c):
    global answer
    answer = 100
    N, M = len(board), len(board[0])
    cards = search_card(board, N, M)
    dfs(board, r, c, N, M, cards, [], 0)
    return answer

B = [
    [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],
    [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]],
    [[1,2,3,5], [4,1,2,6], [3,4,5,0], [6,0,0,0]],
    [[1, 5, 0, 2], [6, 4, 3, 0], [0, 2, 1, 5], [3, 0, 6, 4]],
    [[1,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,1]]
]
R = [1, 0, 0, 0, 0]
C = [0, 1, 0, 0, 0]
for i in range(5):
    print(solution(B[i], R[i], C[i]))
