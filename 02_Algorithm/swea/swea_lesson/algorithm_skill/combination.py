# 재귀적 호출을 이용한 조합 생성
# an : n개의 원소를 가지고 있는 배열
# tr : r개의 크기의 배열, 조합이 임시 저장될 배열
def comb1(n, r):
    if r == 0:
        print(*comb_arr)
    else:
        if n < r:
            return
        else:
            comb_arr[r-1] = arr[n-1]
            comb1(n-1, r-1)
            comb1(n-1, r)


R1 = 3
arr = [0, 1, 2, 3]
comb_arr = [0] * R1
comb1(4, 3)
print('-------------------------')

# 5개중 3개 고르는 조합
N = 5
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            print(i, j, k)

print('----------------------------')

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