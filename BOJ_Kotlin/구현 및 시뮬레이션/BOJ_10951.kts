// A + B - 4
// 분류 : 구현

fun main() = with(System.`in`.bufferedReader()) {
    while (true) {
        val line = readLine() ?: break
        val (a, b) = line.split(" ").map { it.toInt() }
        println(a + b)
    }
}

main()