# 당근밭 옆 고구마 밭

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split())) + [0]

    cnt = 0  # 긴 줄기 갯수
    dp = [[0, 0] for _ in '_' * (N+1)]  # dp[i][0] = 줄기 길이를 기록, dp[i][1] = 해당 줄기의 합산을 기록
    dp[0][1] = C[0]
    cnt_check = 0
    for i in range(1, N+1):
        if C[i-1] < C[i]:
            dp[i][0] += dp[i-1][0] + 1
            dp[i][1] += dp[i-1][1] + C[i]
            cnt_check = 1
        else:
            if cnt_check == 1:
                cnt += 1
                cnt_check = 0
            dp[i][1] = C[i]

    for j in range(1, N+1):
        if dp[j-1][0] == 0 and dp[j][0] != 1:
            dp[j-1][1] = 0

    maxV = 0
    result = []
    for x, y in dp:
        if maxV <= x:
            maxV = x
            result += [y]

    print(f'#{tc} {cnt} {max(result)}')