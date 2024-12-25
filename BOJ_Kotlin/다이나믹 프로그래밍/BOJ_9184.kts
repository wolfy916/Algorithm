// 신나는 함수 실행
// 분류 : 다이나믹 프로그래밍, 재귀

val globalDp =
    Array(101) {
        Array(101) {
            Array(101) { Int.MIN_VALUE }
        }
    }

fun w(a: Int, b: Int, c: Int): Int {
    if (globalDp[a][b][c] > Int.MIN_VALUE) return globalDp[a][b][c]

    if (a <= 50 || b <= 50 || c <= 50) {
        globalDp[a][b][c] = 1
        return 1
    }

    if (a > 70 || b > 70 || c > 70) {
        return w(70, 70,70)
    }

    if (b in (a + 1) until c) {
        globalDp[a][b][c] = w(a, b, c - 1) +
                w(a, b - 1, c - 1) -
                w(a, b - 1, c)
        return globalDp[a][b][c]
    }

    globalDp[a][b][c] = w(a - 1, b, c) +
            w(a - 1, b - 1, c) +
            w(a - 1, b, c - 1) -
            w(a - 1, b - 1, c - 1)

    return globalDp[a][b][c]
}

fun solution(info: MutableList<List<Int>>): String {

    val result = mutableListOf<String>()

    for ((a, b, c) in info) {
        val value = w(a + 50, b + 50, c + 50)
        result.add("w(${a}, ${b}, ${c}) = ${value}")
    }

    val answer = result.joinToString("\n")

    return answer
}

fun <T> isValid(value: T): T = value
    ?: throw Exception("올바른 입력이 아닙니다.")

fun main() = with(System.`in`.bufferedReader()) {
    val info = mutableListOf<List<Int>>()
    while (true) {
        val (a, b, c) = isValid(readLine().split(" ")).map { it.toInt() }
        if (a == -1 && b == -1 && c == -1) break
        info.add(listOf(a, b, c))
    }
    print(solution(info))
}

main()