# 4008. 숫자만들기

# 3 <= N <= 12
# 카드 개수 : N-1
# 숫자들은 1 ~ 9
# 연산자 카드 모두 사용
# 나눗셈 할때 소수점 이하 버림

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


def cal(a, b, s):
    if s == 1:
        return a + b
    elif s == 2:
        return a - b
    elif s == 3:
        return a * b
    else:
        if a // b < 0:
            return a // b + 1
        else:
            return a // b


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    signs = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    P = []
    for i in range(4):
        for j in range(signs[i]):
            P.append(i+1)
    U = []
    perm(0, N-1)
    result = []
    start = nums.pop(0)
    for i in range(len(U)):
        if U[i] == [2, 4, 1, 1]:
            d = 1
        calv = start
        for j in range(N-1):
            calv = cal(calv, nums[j], U[i][j])
        result.append(calv)

    print(f'#{tc} {max(result)-min(result)}')