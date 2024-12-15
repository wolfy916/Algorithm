// 최소힙
// 분류 : 자료구조(힙)

import java.util.*

fun main() = with(System.`in`.bufferedReader()) {
    val N: Int = inputToInt()
    val actions: Array<Int> = Array(N) { inputToInt() }

    print(solution(N, actions))
}

fun inputToInt(): Int = readln().toInt()

fun solution(N: Int, actions: Array<Int>): String {
    val pq = PriorityQueue<Int>() { a, b -> a.compareTo(b) }
    val result = mutableListOf<Int>()

    for (n in actions) {
        if (n > 0)
            pq.add(n)
        else
            result.add(pq.poll() ?: 0)
    }

    return result.joinToString("\n")
}

main()