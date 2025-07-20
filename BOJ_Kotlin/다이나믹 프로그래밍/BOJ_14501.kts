// 퇴사
// 분류 : 다이나믹 프로그래밍

fun solution(n: Int, info: List<List<Int>>): Int {
    val dp = IntArray( n + 2 ) { 0 }

    for (i in n downTo 1) {
        val next = i + info[i - 1][0]
        dp[i] = if (next > n + 1) dp[i + 1] else maxOf(dp[i + 1], dp[next] + info[i - 1][1])
    }

    val answer = dp[1]
    return answer
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val info = List(n) { readLine().split(" ").map{ it.toInt() } }
    print(solution(n, info))
}

main()