// 평균
// 분류 : 구현

fun solution(n: Int, scores: IntArray): String {
    val maxScore = scores.max().toFloat()
    val newScores = FloatArray(n)

    for (i in 0 until n) {
        newScores[i] = scores[i] / maxScore * 100
    }

    val answer = newScores.sum() / n

    return answer.toString()
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val scores = readLine().split(" ").map { it.toInt() }
    print(solution(n, scores.toIntArray()))
}

main()