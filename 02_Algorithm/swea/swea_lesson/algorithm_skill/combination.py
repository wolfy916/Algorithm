def comb(n, lenv, k, s):  # n : 선택 원소 갯수, lenv: arr의 길이, k: 총 선택할 원소 갯수, s: 매 호출된 함수마다 탐색을 시작할 인덱스
    if n == k:
        print(p)
    else:
        for i in range(s, lenv - k + n + 1):
            if used[i] == 0:
                used[i] = 1
                p[n] = arr[i]
                comb(n+1, lenv, k, i+1)
                used[i] = 0


arr = list(map(int, input().split()))
N = len(arr)
k = int(input())
p = [0] * k
used = [0] * N
comb(0, N, k, 0)