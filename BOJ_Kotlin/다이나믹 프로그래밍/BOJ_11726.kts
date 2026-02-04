/**
 * 11726. 2×n 타일링
 * 다이나믹 프로그래밍
 * */

// url: https://www.acmicpc.net/problem/11726

val MOD = 10_007

fun solution(n: Int): Int {
    // n이 2이하면 그대로 값 반환
    if (n <= 2) return n

    val dp = MutableList(n + 1) { 0 }

    // 초기화
    dp[1] = 1
    dp[2] = 2

    for (i in 3..n) {
        // i 번째의 가능한 경우의 수
        // 1. i - 1번째의 경우의 수에서 세로형 타일 1개를 붙이는 경우
        // 2. i - 2번째의 경우의 수에서 가로형 타일 2개를 붙이는 경우
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
    }

    return dp[n]
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    print(solution(n))
}

main()