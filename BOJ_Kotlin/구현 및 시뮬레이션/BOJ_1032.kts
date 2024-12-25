// 명령 프롬프트
// 분류 : 구현

fun solution(n: Int, fileNameArray: Array<String>): String {
    val charArray = fileNameArray[0].toCharArray()

    for (i in 1 until n) {
        val fileName = fileNameArray[i]
        for ((j, v) in fileName.withIndex()) {
            if (charArray[j] != '?' && charArray[j] != v) {
                charArray[j] = '?'
            }
        }
    }

    val answer = charArray.joinToString("")

    return answer
}

fun main() = with(System.`in`.bufferedReader()) {

    fun <T> isValid(value: T): T = value
        ?: throw Exception("올바른 입력이 아닙니다.")

    val n = isValid(readLine().toInt())
    val fileNameArray = Array(n) { isValid(readLine()) }

    print(solution(n, fileNameArray))
}

main()