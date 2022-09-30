
def perm1(i, N):
    if i == N:
        print(P)
    else:
        for j in range(i, N):
            P[i], P[j] = P[j], P[i]
            perm1(i+1, N)
            P[i], P[j] = P[j], P[i]

def perm2(k, r, lenv):
    if k == r:
        print(p2)
    else:
        for i in range(lenv):
            if used[i] == 0:
                used[i] = 1
                if p2[k] != P[i]:
                    p2[k] = P[i]
                perm2(k+1, r, lenv)
                used[i] = 0

def perm3(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in perm3(arr, r-1):
                yield [arr[i]] + next

P = [1, 2, 3]
p2 = [0] * len(P)
used = [0] * len(P)
# perm1(0, len(P))
# print('-----------------')
# perm2(0, 3, len(P))

for arr in perm3(P, 3):
    print(arr)