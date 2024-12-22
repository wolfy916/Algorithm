// ATM
// 분류 : 구현, 누적합

fun solution(n: Int, p: IntArray): String {
    val sortedArray = p.sortedArray()

    for (i in 1 until n) {
        sortedArray[i] += sortedArray[i - 1]
    }

    return sortedArray.sum().toString()
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val p = readLine().split(" ").map { it.toInt() }.toIntArray()
    print(solution(n, p))
}

main()