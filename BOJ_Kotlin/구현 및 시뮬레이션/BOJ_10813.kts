// 공 바꾸기
// 분류 : 구현

fun input() = readLine()!!.split(" ").map { it.toInt() }

fun solution(N: Int, actions: Array<Array<Int>>): String {
    val baskets = Array(N + 1) { i -> i }

    for ((a, b) in actions) {
        val tmp = baskets[a]
        baskets[a] = baskets[b]
        baskets[b] = tmp
    }

    val answer = baskets.slice(1 until N + 1).joinToString(" ")

    return answer
}

fun main() = with(System.`in`.bufferedReader()) {
    val (N, M) = input()
    val actions = Array(M) { Array(2) { 0 } }

    for (i in 0 until M) {
        val (a, b) = input()
        actions[i][0] = a
        actions[i][1] = b
    }

    print(solution(N, actions))
}

main()