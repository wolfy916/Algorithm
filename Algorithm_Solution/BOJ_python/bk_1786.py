# 찾기

def pattern(pat):
    lenV = len(pat)
    table = [0]*lenV
    j = 0
    for i in range(1, lenV):
        while j > 0 and pat[i] != pat[j]:
            j = table[j-1]
        if pat[i] == pat[j]:
            j += 1
            table[i] = j
    return table

def KMP(par, pat):
    table = pattern(pat)
    parent_size = len(par)
    pattern_size = len(pat)
    cnt = 0
    idx_lst = []
    j = 0
    for i in range(parent_size):
        while j > 0 and par[i] != pat[j]:
            j = table[j-1]
        if par[i] == pat[j]:
            if j == pattern_size - 1:
                cnt += 1
                idx_lst.append(i - pattern_size + 2)
                j = table[j]
            else:
                j += 1
    return cnt, idx_lst

T = input()
P = input()
cnt, lst = KMP(T, P)
print(cnt)
for n in lst:
    print(n)