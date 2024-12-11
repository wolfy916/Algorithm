// 지능형 기차 2
// 분류 : 구현

fun main() = with(System.`in`.bufferedReader()) {
    var answer = 0
    var passengers = 0

    for (i in 0 until 10) {
        val (out, come) = readLine()!!.split(" ").map { it.toInt() }
        passengers += come - out
        answer = maxOf(answer, passengers)
    }

    print(answer)
}

main()