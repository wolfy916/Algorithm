def comb(k, r, s, lenv):  # n : 선택 원소 갯수, r: 선택할 총 원소 갯수, s: 매 호출된 함수마다 탐색을 시작할 인덱스
    if k == r:
        print(p1)
    else:
        for i in range(s, lenv - r + k + 1):
            if used[i] == 0:
                used[i] = 1
                p1[k] = arr[i]
                comb(k+1, r, i+1, lenv)
                used[i] = 0


def perm(k, r, lenv):
    if k == r:
        print(p2)
    else:
        for i in range(lenv):
            if used[i] == 0:
                used[i] = 1
                p2[k] = arr[i]
                perm(k+1, r, lenv)
                used[i] = 0


arr = list(map(int, input().split()))
N = len(arr)
R = int(input())  # N:총 선택할 원소의 갯수
p1 = [0] * R
p2 = [0] * R
used = [0] * len(arr)

comb(0, R, 0, N)
print('------------------')
perm(0, R, N)