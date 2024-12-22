// 오등큰수
// 분류 : 자료구조, 스택

fun solution(n: Int, a: Array<Int>): String {

    val f = Array((1e6 + 1).toInt()) { 0 }
    a.forEach { f[it]++ }

    val ngf = Array(n) { 0 }
    val stack = mutableListOf<Int>()
    for (i in n - 1 downTo 0) {
        while(stack.size > 0 && f[a[i]] >= f[stack.last()]) {
            stack.removeLast()
        }

        ngf[i] = if (stack.size > 0) stack.last() else -1
        stack.add(a[i])
    }

    val answer = ngf.joinToString(" ")

    return answer
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val a = readLine().split(" ").map { it.toInt() }.toTypedArray()
    print(solution(n, a))
}

main()