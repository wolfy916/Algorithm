// 색종이 만들기
// 분류 : 분할 정복, 재귀

fun solution(n: Int, paper: List<List<Int>>): String {

    fun isValidPaper(i: Int, j: Int, n: Int): Boolean {
        var prev = paper[i][j]
        for (y in i until i + n) {
            for (x in j until j + n) {
                if (paper[y][x] != prev) return false
                prev = paper[y][x]
            }
        }
        return true
    }

    fun divide(vi: Int, vj:Int, n:Int): Array<Int> {
        val count = arrayOf(0, 0)

        if (isValidPaper(vi, vj, n)) {
            count[paper[vi][vj]]++
        } else {
            val m = n / 2
            for (i in listOf(vi, vi + m)) {
                for (j in listOf(vj, vj + m)) {
                    val result = divide(i, j, m)
                    count[0] += result[0]
                    count[1] += result[1]
                }
            }
        }

        return count
    }

    val count = divide(0, 0, n)
    val answer = count.joinToString("\n")

    return answer
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val paper = List(n) { readLine().split(" ").map { it.toInt() } }
    print(solution(n, paper))
}

main()