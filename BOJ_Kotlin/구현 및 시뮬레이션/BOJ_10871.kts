// X보다 작은 수
// 분류 : 구현 및 시뮬레이션

fun solution(x: Int, numList: List<Int>): String {
    val validList: List<Int> = numList.filter { x > it }
    val answer = validList.joinToString(" ")

    return answer
}

fun main() = with(System.`in`.bufferedReader()) {
    fun input(): List<Int> = readLine().split(" ").map { it.toInt() }
    val (_, x) = input()
    val numList = input()

    print(solution(x, numList))
}

main()