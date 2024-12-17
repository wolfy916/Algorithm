// 집합의 표현
// 분류 : 자료 구조, 분리 집합

class Union(private val n: Int) {
    private val parent = IntArray(n + 1) { it }

    private fun find(num: Int): Int {
        var x = num
        while (parent[x] != x) {
            x = parent[parent[x]]
        }

        parent[num] = x

        return parent[num]
    }

    fun union(x: Int, y: Int) {
        val parX = find(x)
        val parY = find(y)

        if (parX != parY) {
            parent[maxOf(parX, parY)] = minOf(parX, parY)
        }
    }

    fun check(x: Int, y: Int): String {
        val parX = find(x)
        val parY = find(y)

        return if (parX == parY) "YES" else "NO"
    }
}

fun solution(n: Int, orderList: List<List<Int>>): String {
    val result = mutableListOf<String>()
    val union = Union(n)

    for ((a, b, c) in orderList) {
        when (a) {
            0 -> union.union(b, c)
            1 -> result.add(union.check(b, c))
            else -> throw AssertionError()
        }
    }

    return result.joinToString("\n")
}

fun main() = with(System.`in`.bufferedReader()) {
    val (n, m) = readLine().split(" ").map { it.toInt() }
    val orderList = List(m) { readLine().split(" ").map { it.toInt() } }
    print(solution(n, orderList))
}

main()