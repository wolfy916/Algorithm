# 종이의 개수

def divide(arr, n):
    sub_n = n // 3
    if not check(arr):
        for i in range(n):
            for j in range(n):
                if (i % sub_n, j % sub_n) == (0, 0):
                    sub_arr = [arr[k][j:j+sub_n] for k in range(i, i+sub_n)]
                    divide(sub_arr, sub_n)


def check(arr):
    num = arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != num:
                return False
    cnt[num+1] += 1
    return True


N = int(input())
area = [list(map(int, input().split())) for _ in '_'*N]
cnt = [0] * 3
divide(area, N)
print(*cnt)
