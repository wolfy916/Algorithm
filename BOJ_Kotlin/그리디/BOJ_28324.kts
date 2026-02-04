/**
 * 스케이트 연습
 * 실버 4
 * 그리디
 * */

fun solution(n: Int, v: List<Int>): String {
    var prev = 0
    var sumV = 0.toBigInteger()
    for (i in n - 1 downTo 0) {
        prev = minOf(prev + 1, v[i])
        sumV += prev.toBigInteger()
    }
    return sumV.toString()
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val v = readLine().split(" ").map { it.toInt() }
    println(solution(n, v))
}

main()