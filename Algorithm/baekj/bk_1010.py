# 다리 놓기

# 1번 풀이
# factorial 재귀 함수를 사용하여 조합 경우의 수 계산

# factorial
def f(n):
    if n > 1:
        return n * f(n-1)
    return 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 0 < N ≤ M < 30
    mCn = f(M) // (f(M-N) * f(N))     # 조합 경우의 수 계산식
    print(mCn)

# 2번 풀이
# factorial 값을 누적 계산 방식(dp)으로 미리 구현해놓고 값을 참조함

# dp = factorial value list
# memoization : 테스트 케이스가 많을수록, N과 M이 클수록 1번 재귀 풀이보다 훨씬 유리함
dp = [0]*31
dp[0] = dp[1] = 1
for i in range(1, 31):
    dp[i] = i * dp[i-1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 0 < N ≤ M < 30
    mCn = dp[M] // (dp[M-N] * dp[N])  # 조합 경우의 수 계산식
    print(mCn)
