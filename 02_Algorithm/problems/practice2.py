def taxi(start, end, path, charge, n):
    global min_A, min_A_path
    if min_A < charge:
        return

    if start == end:
        if min_A > charge:
            min_A = charge
            min_A_path = path
            return
    else:
        for j in range(1, n + 1):
            w = adjM[start][j]
            if w and not visited_A[j]:
                visited_A[j] = 1
                taxi(j, end, path + [j], charge + w, n)
                visited_A[j] = 0


n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

adjM = [[0]*(n+1) for _ in '_'*(n+1)]
for n1, n2, v in fares:
    adjM[n1][n2] = v
    adjM[n2][n1] = v

min_A = 100000 * (n - 1) + 1
min_A_path = []
visited_A = [0] * (n + 1)
visited_A[s] = 1

taxi(s, a, [s], 0, n)
print(f'A의 최소 요금 : {min_A} 원')
print(f'A의 최소 요금 경로 : {min_A_path}')
