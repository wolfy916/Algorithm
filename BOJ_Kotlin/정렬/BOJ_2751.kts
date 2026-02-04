/**
 * 2751. 수 정렬하기 2
 * 정렬
 * */

// url: https://www.acmicpc.net/problem/2751

fun quickSort(list: List<Int>): List<Int> {
    if (list.size < 2) return list

    val pivot = list.last()
    val (left, right) = list
        .dropLast(1)
        .partition { it < pivot }

    return quickSort(left) + pivot + quickSort(right)
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val list = List(n) { readLine().toInt() }

    print(quickSort(list).joinToString("\n"))
}

main()