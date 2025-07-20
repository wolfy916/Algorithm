// 단어 정렬
// 분류 : 정렬

fun solution(wordList: List<String>): String {
    val wordSet = wordList.toSet()
    val sortedWordList = wordSet.toList()
        .sorted()
        .sortedBy { it.length }
    val answer = sortedWordList.joinToString("\n")
    return answer
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val wordList = List(n) { readLine() }
    print(solution(wordList))
}

main()