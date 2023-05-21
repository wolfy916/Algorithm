# 최대 상금 (그리디 + 완전 탐색)

# 중복 허용 조합
def f(n, cnt, N):       # n : 이전까지의 교환 횟수, cnt : 총 교환 횟수, N : 숫자판 갯수
    global maxV
    if n == cnt:
        tmp = int(''.join(num))
        if maxV < tmp:
            maxV = tmp
    else:
        for i in range(N-1):            # 교환할 두 위치 i, j를 고르는 조합 i < j
            for j in range(i+1, N):
                num[i], num[j] = num[j], num[i]
                tmp = (''.join(num))
                if tmp not in u[n]:
                    u[n] += [tmp]
                    f(n+1, cnt, N)
                num[i], num[j] = num[j], num[i]


for tc in range(1, int(input()) + 1):
    num, cnt = input().split()
    num = list(num)
    cnt = int(cnt)

    N = len(num)
    maxV = 0
    u = [[] for _ in '_'*cnt]
    f(0, cnt, N)

    print(f'#{tc} {maxV}')