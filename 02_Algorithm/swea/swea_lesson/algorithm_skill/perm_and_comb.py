def comb(n, r, s):  # s: 선택할 수 있는 구간의 시작
    if r == 0:
        print(*c)
    else:
        for i in range(s, n-r+1):
            c[r-1] = arr[i]
            comb(n, r-1, i+1)


def perm(i, n, r):
    if i == r:
        print(*p)  # 원하는 작업 수행
    else:
        for j in range(n):
            if not used[j]:    # arr[j]를 사용하지 않았다면
                used[j] = 1    # arr[j]를 사용함으로 표시
                p[i] = arr[j]  # p[i]는 arr[j]로 결정
                perm(i+1, n, r)   # p[i+1] 값을 결정하러 이동
                used[j] = 0    # arr[j]를 다른 자리에서 쓸 수 있도록 해제


arr = list(map(int, input().split()))
N = len(arr)
R = int(input())  # N:총 선택할 원소의 갯수
p = [0] * R
c = [0] * R
used = [0] * len(arr)

comb(N, R, 0)
print('------------------')
perm(0, N, R)