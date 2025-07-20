// 숫자의 개수
// 분류 : 구현

fun solution(a: Int, b: Int, c: Int): String {
    val list = (a * b * c).toString().split("")
    val arr: Array<Int> = Array(10) { 0 }
    for (i in 1 until list.size - 1) { arr[list[i].toInt()]++ }
    val answer = arr.joinToString("\n")
    return answer
}

fun main() = with(System.`in`.bufferedReader()) {
    val a = readLine().toInt()
    val b = readLine().toInt()
    val c = readLine().toInt()
    print(solution(a, b, c))
}

main()