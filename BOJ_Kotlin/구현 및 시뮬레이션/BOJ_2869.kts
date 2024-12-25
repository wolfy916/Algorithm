// 달팽이는 올라가고 싶다
// 분류 : 구현

import kotlin.math.ceil

fun solution(a: Double, b: Double, v: Double): String {
    val day = ceil((v - a) / (a - b)) + 1
    val answer = day.toInt().toString()
    return answer
}

fun main() = with(System.`in`.bufferedReader()) {

    fun <T> isValid(value: T): T = value
        ?: throw Exception("올바른 입력이 아닙니다.")

    val (a, b, v) = isValid(readLine().split(" ").map { it.toDouble() })

    print(solution(a, b, v))
}

main()