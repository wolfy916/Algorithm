def comb(n, r, s, lenv):  # n : 선택 원소 갯수, r: 선택할 총 원소 갯수, s: 매 호출된 함수마다 탐색을 시작할 인덱스
    if n == r:
        print(p1)
    else:
        for i in range(s, lenv - r + n + 1):
            if used[i] == 0:
                used[i] = 1
                p1[n] = arr[i]
                comb(n+1, r, i+1, lenv)
                used[i] = 0


def perm(n, r, lenv):
    if n == r:
        print(p2)
    else:
        for i in range(lenv):
            if used[i] == 0:
                p2[n] = arr[i]
                used[i] = 1
                perm(n+1, r, lenv)
                used[i] = 0


arr = list(map(int, input().split()))
lenV = int(input())  # N:총 선택할 원소의 갯수
p1 = [0] * lenV
p2 = [0] * lenV
used = [0] * len(arr)

comb(0, lenV, 0, len(arr))
print('------------------')
perm(0, lenV, len(arr))