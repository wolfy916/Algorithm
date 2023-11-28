from heapq import heappop, heappush


def solution(board):
    answer = 0
    N = len(board)
    delta1 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    delta2 = [((-1, 0), (1, 0)), ((0, -1), (0, 1))]
    hq = [(0, 0, 0, 0, 1)]
    while hq:
        cnt, li, lj, ri, rj = heappop(hq)
        if (li, lj) == (N - 1, N - 1) or (ri, rj) == (N - 1, N - 1):
            answer = cnt
            break
        # 이동
        for di, dj in delta1:
            nli, nlj = li + di, lj + dj
            if nli < 0 or nlj < 0 or nli >= N or nlj >= N: continue
            if board[nli][nlj] == 1: continue
            nri, nrj = ri + di, rj + dj
            if nri < 0 or nrj < 0 or nri >= N or nrj >= N: continue
            if board[nri][nrj] == 1: continue
            heappush(hq, (cnt + 1, nli, nlj, nri, nrj))
        # 회전
        k = abs(li - ri)  # 0: 가로 배치, 1: 세로 배치
        for di, dj in delta2[k]:
            nli, nlj = li + di, lj + dj
            if nli < 0 or nlj < 0 or nli >= N or nlj >= N: continue
            if board[nli][nlj] == 1: continue
            nri, nrj = ri + di, rj + dj
            if nri < 0 or nrj < 0 or nri >= N or nrj >= N: continue
            if board[nri][nrj] == 1: continue
            heappush(hq, (cnt + 1, nri, nrj, ri, rj))
            heappush(hq, (cnt + 1, li, lj, nli, nlj))

    return answer

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))