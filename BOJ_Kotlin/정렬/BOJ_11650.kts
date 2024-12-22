// 좌표 정렬하기
// 분류 : 정렬

fun solution(coords: List<List<Int>>): String {
    val sortedCoords = coords.sortedWith(compareBy({ it[0] }, { it[1] }))

    return sortedCoords.joinToString("\n") { it.joinToString(" ") }
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val coords = List(n) { readLine().split(" ").map { it.toInt() } }
    print(solution(coords))
}

main()