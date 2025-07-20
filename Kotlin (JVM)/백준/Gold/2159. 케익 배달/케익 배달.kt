import kotlin.math.abs

// 케익 배달
// 난이도 : 골드 3
// 분류 : 다이나믹 프로그래밍

fun solution(n: Int, coords: Array<List<Long>>): Long  {
    val dp = Array(n + 1) { LongArray(5) { Long.MAX_VALUE } }
    val dx = listOf(0, -1, 0, 1, 0)
    val dy = listOf(0, 0, 1, 0, -1)

    for (k in 0 until 5) {
        val nx = coords[1][0] + dx[k]
        val ny = coords[1][1] + dy[k]
        if (nx < 0 || nx > 1e5 || ny < 0 || ny > 1e5) continue
        dp[1][k] = abs(coords[0][0] - nx) + abs(coords[0][1] - ny)
    }

    for (i in 2 until n + 1) {
        val minDis = minOf(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2], dp[i - 1][3], dp[i - 1][4])
        for (j in 0 until 5) {
            if (dp[i - 1][j] != minDis) continue
            val x = coords[i - 1][0] + dx[j]
            val y = coords[i - 1][1] + dy[j]
            for (k in 0 until 5) {
                val nx = coords[i][0] + dx[k]
                val ny = coords[i][1] + dy[k]
                if (nx < 0 || nx > 1e5 || ny < 0 || ny > 1e5) continue
                dp[i][k] = minOf(dp[i][k], dp[i - 1][j] + abs(x - nx) + abs(y - ny))
            }
        }
    }

    return minOf(dp[n][0], dp[n][1], dp[n][2], dp[n][3], dp[n][4])
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val coords = Array(n + 1) { readLine().split(" ").map { it.toLong() } }
    print(solution(n, coords))
}