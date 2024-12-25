// 찾기
// 분류 : 문자열, KMP

// [A] 전처리 함수
fun pattern(m: Int, p: String): Array<Int> {
    val table = Array(m) { 0 }
    var j = 0
    for (i in 1 until m) {
        while (j > 0 && p[i] != p[j]) {
            j = table[j - 1]
        }
        if (p[i] == p[j]) {
            j += 1
            table[i] = j
        }
    }
    return table
}

// [B] KMP 알고리즘
fun kmp(t: String, p: String): Pair<Int, List<Int>> {
    val (n, m) = Pair(t.length, p.length)
    val table = pattern(m, p)
    val idxList = mutableListOf<Int>()

    var count = 0
    var j = 0
    for (i in 0 until n) {
        while (j > 0 && t[i] != p[j]) {
            j = table[j - 1]
        }
        if (t[i] == p[j]) {
            if (j == m - 1) {
                count += 1
                j = table[j]
                idxList.add(i - m + 2)
            } else {
                j += 1
            }
        }
    }
    return Pair(count, idxList)
}

fun solution(t: String, p: String): String {
    val (count, idxList) = kmp(t, p)
    val answer = "${count}\n" + idxList.joinToString("\n")
    return answer
}

fun <T> isValid(value: T): T = value
    ?: throw Exception("올바른 입력이 아닙니다.")

fun main() = with(System.`in`.bufferedReader()) {
    val t = isValid(readLine())
    val p = isValid(readLine())
    print(solution(t, p))
}

main()