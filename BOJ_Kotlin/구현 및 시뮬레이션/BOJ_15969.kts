// 행복
// 분류 : 구현

fun solution(scores: Array<Int>): String {
    val maxV = scores.max()
    val minV = scores.min()
    val answer = (maxV - minV).toString()
    return answer
}

fun main() = with(System.`in`.bufferedReader()) {

    fun <T> isValid(value: T): T = value
        ?: throw Exception("올바른 입력이 아닙니다.")

    val n = isValid(readLine()?.toInt())
    val scores = isValid(
        readLine()?.split(" ")
        ?.map { it.toInt() }
        ?.toTypedArray()
    )

    print(solution(scores!!))
}

main()