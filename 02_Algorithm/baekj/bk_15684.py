# 사다리 조작

# n개에서 r개를 고르는 조합 (재귀)
def comb(n, r, s, t):  # s: 선택할 수 있는 구간의 시작
    global result
    if r == 0:
        test = []
        for num in comb_arr:
            n_i = num//(N-1) + 1
            n_j = num%(N-1) + 1
            area[n_i][n_j] = 1
            area[n_i][n_j+1] = -1
            test.append((n_i, n_j))
        if path_check():
            result = t
        else:
            for n_i, n_j in test:
                area[n_i][n_j] = 0
                area[n_i][n_j + 1] = 0
    else:
        for i in range(s, n-r+1):
            comb_arr[r-1] = ladder[i]
            comb(n, r-1, i+1, t)


def path_check():
    for j in range(N):
        s_i, s_j = 0, j
        while s_i != H+1:
            if area[s_i][s_j]:
                s_j += area[s_i][s_j]
            s_i += 1
        if s_j != j:
            return False
    return True


# 2 ≤ N ≤ 10, 1 ≤ H ≤ 30, 0 ≤ M ≤ (N-1)×H
N, M, H = map(int, input().split())
area = [[0]*(N+1) for _ in '_'*(H+2)]
ladder = list(range((N-1)*H))

for _ in '_'*M:
    # 1 ≤ a ≤ H, 1 ≤ b ≤ N-1
    a, b = map(int, input().split())
    area[a][b] = 1
    area[a][b+1] = -1
    Idx = (a-1)*(N-1)+b-1
    if Idx in ladder:
        ladder.remove(Idx)
    if b == 1 and Idx+1 in ladder:
        ladder.remove(Idx+1)
    elif b == N-1 and Idx-1 in ladder:
        ladder.remove(Idx-1)
    else:
        if Idx+1 in ladder:
            ladder.remove(Idx+1)
        if Idx-1 in ladder:
            ladder.remove(Idx-1)

result = -1
if not path_check():
    for i in range(1, 4):
        comb_arr = [0] * i
        comb(len(ladder), i, 0, i)
        if result == i:
            break
else:
    result = 0

print(result)