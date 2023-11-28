'''
동전 2 - 백준(골드5)
분류 : DP
'''
def solution(n, k, coins):
    INF = float('inf')
    dp = [INF] * (k + 1)
    coins = list(set(coins))
    for coin in coins:
        if coin > k: continue
        dp[coin] = 1

    for price in range(k + 1):
        if price == INF: continue
        for coin in coins:
            if price + coin > k: continue
            dp[price + coin] = min(dp[price + coin], dp[price] + 1)

    return dp[k] if dp[k] != INF else -1

if __name__ == '__main__':
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    print(solution(n, k, coins))