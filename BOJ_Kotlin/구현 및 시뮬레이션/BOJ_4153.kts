// 직각삼각형
// 분류 : 구현
import kotlin.math.*

fun solution(a: Float, b: Float, c: Float): String {
    var isValid = false
    isValid = a.pow(2) + b.pow(2) == c.pow(2) || isValid
    isValid = b.pow(2) + c.pow(2) == a.pow(2) || isValid
    isValid = c.pow(2) + a.pow(2) == b.pow(2) || isValid
    val answer = if (isValid) "right" else "wrong"
    return answer
}

fun main() = with(System.`in`.bufferedReader()) {
    while (true) {
        val (a, b, c) = readLine().split(" ").map{ it.toFloat() }
        if (a == 0F) break
        println(solution(a, b, c))
    }
}

main()