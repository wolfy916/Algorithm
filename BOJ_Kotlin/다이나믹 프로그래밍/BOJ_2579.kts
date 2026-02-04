/**
 * 2579. 계단 오르기
 * 다이나믹 프로그래밍
 * */

// url: https://www.acmicpc.net/problem/2579

fun solution(n: Int, stairs: List<Int>): Int {
    // 계단이 2개이하면 합을 그대로 반환
    if (n <= 2) return stairs.sum()

    // i: i번째 계단, j: 이전에 연속된 계단을 올랐는지 여부
    // dp[i][j] = i, j 조건으로 도달했을때의 최댓값
    val dp = List(n) { intArrayOf(0, 0) }

    // 초기화
    dp[0][0] = stairs[0] // 바로 첫번째 계단을 밞음
    dp[1][0] = stairs[1] // 바로 두번째 계단을 밟음
    dp[1][1] = stairs[0] + stairs[1] // 연속해서 첫번째, 두번째 계단을 밟음

    for (i in 2 until n) {
        // 1. 두 계단씩 오른 경우
        dp[i][0] = stairs[i] + dp[i - 2].max()
        // 2. 한 계단씩 오른 경우
        dp[i][1] = stairs[i] + dp[i - 1][0]
    }

    // 마지막 계단의 각 조건별 값 중 최댓값을 반환
    return dp.last().max()
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val stairs = List(n) { readLine().toInt() }
    print(solution(n, stairs))
}

main()