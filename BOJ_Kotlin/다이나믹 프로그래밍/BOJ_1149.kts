// RGB거리
// 분류 : 다이나믹 프로그래밍

fun solution(n: Int, costs: List<Array<Int>>): String {

    for (i in 1 until n) {
        costs[i][0] += minOf(costs[i - 1][1], costs[i - 1][2])
        costs[i][1] += minOf(costs[i - 1][2], costs[i - 1][0])
        costs[i][2] += minOf(costs[i - 1][0], costs[i - 1][1])
    }

    val minCost = costs[n - 1].min()
    val answer = minCost.toString()

    return answer
}

fun <T> isValid(value: T): T = value
    ?: throw Exception("올바른 입력이 아닙니다.")

fun main() = with(System.`in`.bufferedReader()) {
    val n = isValid(readLine().toInt())
    val costs = List(n) {isValid(
        readLine().split(" ")
            .map { it.toInt() }
            .toTypedArray()
    )}

    print(solution(n, costs))
}

main()