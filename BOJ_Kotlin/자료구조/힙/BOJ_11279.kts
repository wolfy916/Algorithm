/**
 * 최대 힙
 * 실버 2
 * 우선순위 큐
 * */

class MaxHeap {
    private val heap = mutableListOf<Int>()
    val size get() = heap.size
    val maxValue get() = heap.first()

    private fun getLeftChd(par: Int) = par * 2 + 1
    private fun getPar(chd: Int) = (chd - 1) / 2

    private fun swap(a: Int, b: Int) {
        val temp = heap[a]
        heap[a] = heap[b]
        heap[b] = temp
    }

    private fun siftDown() {
        var cur = 0; var chd = 1 // siftDown이 실행되는 시점에 heap.size는 2이상임
        while (chd < size) {
            val rightChd = chd + 1
            if (rightChd < size && heap[chd] < heap[rightChd]) {
                chd = rightChd
            }
            if (heap[cur] < heap[chd]) {
                swap(cur, chd)
                cur = chd
                chd = getLeftChd(cur)
            } else break
        }
    }

    private fun siftUp() {
        var cur = size - 1
        while (0 < cur) {
            val par = getPar(cur)
            if (heap[par] < heap[cur]) {
                swap(cur, par)
                cur = par
            } else break
        }
    }

    fun add(x: Int) {
        heap.add(x)
        siftUp()
    }

    fun poll(): Int {
        if (heap.isEmpty()) return 0 // 문제 출력 조건
        if (size == 1) return heap.removeLast()

        val data = heap.first()
        heap[0] = heap.removeLast()

        siftDown()

        return data
    }
}

fun solution(nums: List<Int>): String {
    val priorityQueue = MaxHeap()
    val outputList = mutableListOf<Int>()

    nums.forEach {
        if (it > 0) priorityQueue.add(it)
        else outputList.add(priorityQueue.poll())
    }

    return outputList.joinToString("\n")
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val nums = List(n) { readLine().toInt() }
    println(solution(nums))
}

main()