// 운동
// 분류 : 최단경로, 플로이드 워셜

fun solution(v: Int, e:Int, edges: List<List<Int>>): Int {
    val MAX = Int.MAX_VALUE / 2
    val adjM = Array(v + 1) { IntArray(v + 1) { MAX } }

    for ((a, b, c) in edges) {
        adjM[a][b] = c
    }

    for (r in 1 until v + 1) {
        for (a in 1 until v + 1) {
            for (b in 1 until v + 1) {
                adjM[a][b] = adjM[a][b].coerceAtMost(
                    adjM[a][r] + adjM[r][b]
                )
            }
        }
    }

    var minV = MAX
    for (i in 1 until v + 1) {
        minV = minV.coerceAtMost(adjM[i][i])
    }

    val answer = if (minV == MAX) -1 else minV
    return answer
}

fun main() = with(System.`in`.bufferedReader()) {
    val (v, e) = readLine().split(" ").map{ it.toInt() }
    val edges = List(e) { readLine().split(" ").map { it.toInt() }}
    print(solution(v, e, edges))
}

main()