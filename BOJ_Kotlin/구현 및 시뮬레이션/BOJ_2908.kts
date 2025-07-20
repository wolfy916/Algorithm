// 상수
// 분류 : 구현

fun solution(a: String, b: String): String {
    val toReverseInt = { n: String -> n.reversed().toInt() }
    val answer = maxOf(
        toReverseInt(a),
        toReverseInt(b)
    ).toString()
    return answer
}

fun main() = with(System.`in`.bufferedReader()) {
    val (a, b) = readLine().split(" ")
    print(solution(a, b))
}

main()