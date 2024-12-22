// 색종이
// 분류 : 구현

fun solution(n: Int, coords: List<List<Int>>): String {
    val sortedList = coords.sortedBy { it[0] }
    val yCoords = Array(101) { 0 }
    var answer = 0
    var idx = 0

    for (x in 0 until 100) {
        while (idx < n && sortedList[idx][0] == x) {
            for (y in sortedList[idx][1] until minOf(sortedList[idx][1] + 10, 101)) {
                yCoords[y] = 10
            }
            idx++
        }

        for (y in 0 until 100) {
            if (yCoords[y] > 0) {
                answer++
                yCoords[y]--
            }
        }
    }

    return answer.toString()
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val coords = List(n) { readLine().split(" ").map { it.toInt() } }
    print(solution(n, coords))
}

main()