// 배열 돌리기 1
// 분류 : 구현

fun main() = with(System.`in`.bufferedReader()) {
    val (n, m, r) = inputToList()
    val array: Array<Array<Int>> = Array(n) { Array(m) { 0 } }

    for (i in 0 until n) {
        val line = inputToList()
        for (j in 0 until m) {
            array[i][j] = line[j]
        }
    }

    print(solution(n, m, r, array))
}

fun inputToList(): List<Int> = readln().split(" ").map { it.toInt() }

fun isValidIdx(i: Int, j: Int, n: Int, m: Int, s: Int): Boolean {
    return if (i < s || j < s || i >= n - s || j >= m - s) false
    else true
}

fun solution(n: Int, m: Int, r:Int, array: Array<Array<Int>>): String {
    val di = listOf(1, 0, -1, 0)
    val dj = listOf(0, 1, 0, -1)
    val numberOfSquare = minOf(n, m) / 2
    val newArray: Array<Array<Int>> = Array(n) { Array(m) { 0 } }

    for (s in 0 until numberOfSquare) {
        val squareSize = (n - s * 2) * 2 + (m - s * 2) * 2 - 4
        val square: List<Array<Int>> = List(squareSize) { arrayOf(0, 0) }
        var i = s
        var j = s
        var k = 0

        for (idx in 0 until  squareSize) {
            square[idx][0] = i
            square[idx][1] = j

            if (!isValidIdx(i + di[k], j + dj[k], n, m, s)) {
                k = (k + 1) % 4
            }

            i += di[k]
            j += dj[k]
        }

        for (idx in 0 until squareSize) {
            val (vi, vj) = square[idx]
            val (ni, nj) = square[(idx + r) % squareSize]
            newArray[ni][nj] = array[vi][vj]
        }
    }

    val answer = newArray.map { it.joinToString(" ") }.joinToString("\n")

    return answer
}

main()