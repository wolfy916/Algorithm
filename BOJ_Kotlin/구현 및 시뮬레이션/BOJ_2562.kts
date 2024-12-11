// 최댓값
// 분류 : 구현

fun isValid(n: Int?): Boolean {
    if (n == null) return false
    else if (n < 1 || n > 100) return false
    else return true
}

fun solution(list: List<Int?>): String {
    var maxV: Int = 0
    var maxIdx: Int = -1

    list.forEachIndexed() { idx, value ->
        if (isValid(value) && value!! > maxV) {
            maxV = value
            maxIdx = idx
        }
    }

    val answer = "${maxV}\n${maxIdx + 1}"

    return answer
}

fun main() = with(System.`in`.bufferedReader()) {
    val list: List<Int?> = List(9) { readLine()?.toInt() }
    solution(list).let { print(it) }
}

main()