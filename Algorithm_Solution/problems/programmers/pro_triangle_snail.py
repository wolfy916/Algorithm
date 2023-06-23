# 삼각 달팽이
def solution(n):
    answer = []
    table = [[0] * n for _ in '_' * n]
    i = j = 0
    num = 1
    table[i][j] = num
    delta = [(1, 0), (0, 1), (-1, -1)]
    delta_idx = 0
    N = (n+1) * n // 2
    while num < N:
        di, dj = delta[delta_idx]
        if not (0 <= i+di < n and 0 <= j+dj < n) or table[i+di][j+dj] != 0:
            delta_idx = (delta_idx + 1) % 3
        else:
            i += di
            j += dj
            num += 1
            table[i][j] = num

    for i in range(n):
        for j in range(n):
            if table[i][j]:
                answer.append(table[i][j])
            else:
                break

    return answer

print(solution(4))