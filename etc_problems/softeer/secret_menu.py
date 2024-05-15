# 비밀 메뉴
# kmp

def compute_table(pattern):
    j = 0
    table = [0] * M
    for i in range(1, M):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table

def kmp(parent, pattern):
    table = compute_table(pattern)
    j = 0
    for i in range(N):
        while 0 < j and parent[i] != pattern[j]:
            j = table[j - 1]
        if parent[i] == pattern[j]:
            if j == M - 1:
                return 'secret'
            else:
                j += 1
    return 'normal'

M, N, K = map(int, input().split())
secret = list(map(int, input().split()))
control = list(map(int, input().split()))

if N < M:
    print('normal')
else:
    print(kmp(control, secret))
