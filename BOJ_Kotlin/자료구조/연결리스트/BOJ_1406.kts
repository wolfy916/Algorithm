/**
 * 에디터
 * 실버2
 * 연결리스트
 */

class Node<T>(
    var data: T,
    var prev: Node<T>? = null,
    var next: Node<T>? = null
)

class DoublyLinkedList<T>(
    dataList: List<T>? = null
) {
    private var head: Node<T>? = null
    private var tail: Node<T>? = null

    /**
     * 커서 왼쪽의 노드를 가리킴 (커서가 맨 앞이면 null)
     */
    private var cursor: Node<T>? = null

    init { dataList?.let { addNodeList(it) } }

    private fun addNodeList(list: List<T>) {
        if (list.isEmpty()) return

        head = Node(list.first())
        var current = head
        for (i in 1 until list.size) {
            val newNode = Node(list[i], current)
            current!!.next = newNode
            current = newNode
        }
        tail = current
        cursor = tail // 초기 커서: 문장 맨 뒤(왼쪽 노드 = 마지막 문자)
    }

    fun processCommand(command: String) {
        when (command[0]) {
            'L' -> moveLeft()
            'D' -> moveRight()
            'B' -> deleteLeft()
            'P' -> addLeft(command[2] as T) // "P x" 형태이므로 index 2가 문자
        }
    }

    private fun moveLeft() {
        // 커서가 null(맨 앞)이면 무시, 아니면 왼쪽으로 한 칸
        if (cursor != null) cursor = cursor?.prev
    }

    private fun moveRight() {
        // 만약 커서가 null(맨 앞)이라면 head로 (한 칸 오른쪽)
        // 아니면 cursor.next가 있으면 그걸로, 없으면(=맨 뒤) 유지
        cursor = if (cursor == null) {
            head
        } else {
            if (cursor?.next != null) cursor?.next else cursor
        }
    }

    private fun deleteLeft() {
        // 커서 왼쪽 노드가 없으면 무시
        val target = cursor ?: return
        val prevNode = target.prev
        val nextNode = target.next

        if (prevNode != null) prevNode.next = nextNode else head = nextNode
        if (nextNode != null) nextNode.prev = prevNode else tail = prevNode

        cursor = prevNode
    }

    private fun addLeft(data: T) {
        val leftNode = cursor
        val rightNode = if (cursor == null) head else cursor?.next

        val newNode = Node(data, leftNode, rightNode)

        if (leftNode != null) leftNode.next = newNode else head = newNode
        if (rightNode != null) rightNode.prev = newNode else tail = newNode

        cursor = newNode
    }

    override fun toString(): String {
        val sb = StringBuilder()
        var cur = head
        while (cur != null) {
            sb.append(cur.data)
            cur = cur.next
        }
        return sb.toString()
    }
}

fun solution(sentence: String, commands: List<String>): String {
    val list = DoublyLinkedList(sentence.toList())
    commands.forEach { list.processCommand(it) }
    return list.toString()
}

fun main() = with(System.`in`.bufferedReader()) {
    val sentence = readLine()!!
    val n = readLine()!!.toInt()
    val commands = List(n) { readLine()!! }
    println(solution(sentence, commands))
}

main()
