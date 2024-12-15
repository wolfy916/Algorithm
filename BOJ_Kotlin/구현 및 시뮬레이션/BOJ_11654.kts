// 아스키 코드
// 분류 : 구현

fun main() = with(System.`in`.bufferedReader()) {
    val str = readLine().toCharArray()
    println(str[0].toInt())
}

main()