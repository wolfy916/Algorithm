/**
 * 전화번호 목록
 * 골드 4
 * Trie
 * */

class TrieNode {
    val nextNode = mutableMapOf<Char, TrieNode?>()
}

class Trie {
    companion object {
        private const val END_KEY = '*'
    }
    private val rootNode = TrieNode()

    fun insert(word: String) {
        var currentNode: TrieNode? = rootNode

        for (char in word) {
            currentNode = currentNode
                ?.nextNode
                ?.getOrPut(char) { TrieNode() }
        }

        currentNode?.nextNode?.put(END_KEY, null)
    }

    // 문제에서 안쓰이는데 작성해봄
    fun search(word: String): Boolean {
        var currentNode: TrieNode = rootNode

        for (char in word) {
            currentNode = currentNode
                .nextNode[char]
                ?: return false
        }

        return currentNode.nextNode.keys.contains(END_KEY)
    }

    fun isConsistent(currentNode: TrieNode = rootNode): Boolean {
        // keys가 '*'를 포함하고, keys.size가 2이상이면 일관성이 없음
        var result = !(currentNode.nextNode.keys.contains(END_KEY)
                && currentNode.nextNode.keys.size >= 2)

        for (value in currentNode.nextNode.values) {
            if (!result) break
            value?.let {
                result = isConsistent(it)
            }
        }

        return result
    }
}

fun solution(phones: List<String>): String {
    val trie = Trie()

    phones.forEach { trie.insert(it) }

    return when(trie.isConsistent()) {
        true -> "YES"
        false -> "NO"
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val t = readLine().toInt()
    repeat(t) {
        val n = readLine().toInt()
        val phones = List(n) { readLine() }
        println(solution(phones))
    }
}

main()