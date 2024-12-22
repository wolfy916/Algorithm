// 수 정렬하기
// 분류 : 정렬, 구현

fun solution(n: Int, list: List<Int>): String {
    val answer = list.sorted().joinToString("\n")
    return answer
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine()?.toInt() ?: throw Exception("올바른 입력이 아닙니다.")
    val list = List(n) { readLine().toInt() }
    print(solution(n, list))
}

main()