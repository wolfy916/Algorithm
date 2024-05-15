def perm(i, k, r):
    if i == r:
        print(*p)  # 원하는 작업 수행
    else:
        for j in range(k):
            if not used[j]:    # arr[j]를 사용하지 않았다면
                used[j] = 1    # arr[j]를 사용함으로 표시
                p[i] = arr[j]  # p[i]는 arr[j]로 결정
                perm(i+1, k, r)   # p[i+1] 값을 결정하러 이동
                used[j] = 0    # arr[j]를 다른 자리에서 쓸 수 있도록 해제


# nPr
N = int(input())  # n
R = int(input())  # r
arr = list(range(1, N+1))
used = [0] * N
p = [0] * R
perm(0, N, R)
