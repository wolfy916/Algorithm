// LCS
// 분류 : 다이나믹 프로그래밍, LCS(최장 공통 부분 수열)

// LCS 길이 문제

fun solution(str1: String, str2: String): String {
    val n = str1.length
    val m = str2.length
    val dp = Array(n + 1) { Array(m + 1) { 0 } }

    for (i in 1 until n + 1) {
        for (j in 1 until m + 1) {
            if (str1[i - 1] == str2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1
            } else {
                dp[i][j] = maxOf(dp[i - 1][j], dp[i][j - 1])
            }
        }
    }

    val answer = dp[n][m].toString()

    return answer
}

fun main() = with(System.`in`.bufferedReader()) {

    fun <T> isValid(value: T): T = value
        ?: throw Exception("올바른 입력이 아닙니다.")

    val str1 = readLine()
    val str2 = readLine()

    print(solution(str1, str2))
}

main()