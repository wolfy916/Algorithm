// 전자레인지
// 분류 : 그리디, 구현

fun solution(time: Int): String {
    var t = time
    val btns = arrayOf(0, 0, 0)

    btns[0] = t / 300
    t %= 300

    btns[1] = t / 60
    t %= 60

    btns[2] = t / 10
    t %= 10

    return if (t == 0) btns.joinToString(" ") else "-1"
}

fun main() = with(System.`in`.bufferedReader()) {
    val time = readLine()?.toInt() ?: throw Exception("올바른 입력이 아닙니다.")
    print(solution(time))
}

main()