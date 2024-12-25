// 그릇
// 분류 : 구현

fun solution(parentheses: String): String {
    var height = 10

    for (i in 1 until parentheses.length) {
        height += if (parentheses[i - 1] == parentheses[i]) {
            5
        } else {
            10
        }
    }

    val answer = height.toString()

    return answer
}

fun main() = with(System.`in`.bufferedReader()) {

    fun <T> isValid(value: T): T = value
        ?: throw Exception("올바른 입력이 아닙니다.")

    val parentheses = isValid(readLine())

    print(solution(parentheses))
}

main()