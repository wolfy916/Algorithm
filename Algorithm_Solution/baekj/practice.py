def solution():
    while True:
        n, k = map(int, input().split())
        if n == 0 and k == 0:
            break
        arr = list(map(int, input().split()))
        dp = [[0] * (k + 1) for _ in range(n)]
        count = 0
        for i in range(n):
            dp[i][1] = 1
            for j in range(i):
                if arr[j] >= arr[i]:
                    continue
                tmp = min(i + 1, k)
                for c in range(1, tmp):
                    dp[i][c + 1] += dp[j][c]
            count += dp[i][k]
        print(count)

solution()