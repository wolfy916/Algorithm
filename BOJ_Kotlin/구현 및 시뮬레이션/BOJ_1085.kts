// 직사각형에서 탈출
// 분류 : 구현

fun solution(x: Int, y: Int, w: Int, h: Int): String {
    val answer = minOf(w - x, h - y, x, y).toString()
    return answer
}

fun main() = with(System.`in`.bufferedReader()) {
    val (x, y, w, h) = readLine().split(" ").map { it.toInt() }
    print(solution(x, y, w, h))
}

main()