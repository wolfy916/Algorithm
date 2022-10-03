# n개에서 r개를 고르는 조합 (재귀)
def comb2(n, r, s):  # s: 선택할 수 있는 구간의 시작
    if r == 0:
        print(*comb_arr2)
    else:
        for i in range(s, n-r+1):
            comb_arr2[r-1] = arr2[i]
            comb2(n, r-1, i+1)


R2 = 3
arr2 = [1, 3, 5, 7]
comb_arr2 = [0] * R2

comb2(len(arr2), R2, 0)