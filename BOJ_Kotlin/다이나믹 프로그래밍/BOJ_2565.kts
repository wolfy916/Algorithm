// 전깃줄
// 분류 : 다이나믹 프로그래밍

fun solution(size:Int, arr: Array<Array<Int>>): Int {

    val dp: Array<Int> = Array(size) { 1 }

    for (i in 1 until size) {
        var maxV = 0

        for (j in 0 until i) {
            if (arr[j][1] < arr[i][1]) {
                maxV = maxOf(maxV, dp[j])
            }
        }

        dp[i] += maxV
    }

    val answer = size - dp.max()

    return answer
}

fun main() = with(System.`in`.bufferedReader()) {

    val size = readLine().toInt()
    val arr: Array<Array<Int>> = Array(size) { arrayOf(0, 0) }

    for (i:Int in 0 until size) {
        val (a, b) = readLine().split(" ").map { it.toInt() }
        arr[i][0] = a - 1
        arr[i][1] = b - 1
    }

    arr.sortBy { it[0] }

    print(solution(size, arr))
}

main()