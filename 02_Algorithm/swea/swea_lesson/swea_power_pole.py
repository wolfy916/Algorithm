# 전봇대

for tc in range(1, int(input())+1):
    N = int(input())
    lines = []
    cnt = 0
    for _ in '_'*N:
        a, b = map(int, input().split())
        if lines:
            for a_n, b_n in lines:
                if a > a_n and b < b_n:
                    cnt += 1
                elif a < a_n and b > b_n:
                    cnt += 1
            lines += [[a, b]]
        else:
            lines += [[a, b]]

    print(f'#{tc} {cnt}')