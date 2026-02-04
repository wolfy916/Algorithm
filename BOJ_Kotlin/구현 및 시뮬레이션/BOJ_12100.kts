/**
 * 2048 (Easy)
 * 골드 1
 * 구현
 * */

enum class Direction(val i: Int, val j: Int){
    UP(-1, 0), DOWN(1, 0),
    LEFT(0, -1), RIGHT(0, 1);
}

inline fun getAllIdxByDirection(n: Int, d: Direction, block: (Int, Int) -> Unit) {
    when (d) {
        Direction.UP -> {
            for (j in 0 until n) {
                for (i in 0 until n) {
                    block(i, j)
                }
            }
        }
        Direction.DOWN -> {
            for (j in 0 until n) {
                for (i in n - 1 downTo 0) {
                    block(i, j)
                }
            }
        }
        Direction.LEFT -> {
            for (i in 0 until n) {
                for (j in 0 until n) {
                    block(i, j)
                }
            }
        }
        Direction.RIGHT -> {
            for (i in 0 until n) {
                for (j in n - 1 downTo 0) {
                    block(i, j)
                }
            }
        }
    }
}

data class Task(
    val i: Int, val j: Int,
    val ni: Int, val nj: Int,
    val score: Int,
)

fun solution(n: Int, board: List<IntArray>): Int {
    val isMerged = List(n) { BooleanArray(n){ false } }
    fun List<BooleanArray>.init() = this.forEach { it.fill(false) }
    var maxScore = board.maxOf { it.max() }

    fun isValid(i: Int, j: Int) = !(i < 0 || i >= n || j < 0 || j >= n)

    fun generateTask(i: Int, j: Int, d: Direction, s: Int): Task? {
        var ni = i; var nj = j
        while (isValid(ni + d.i, nj + d.j)) {
            val nextValue = board[ni + d.i][nj + d.j]
            if (nextValue == 0) {
                ni += d.i; nj += d.j
            } else if (nextValue == s && !isMerged[ni + d.i][nj + d.j]) {
                ni += d.i; nj += d.j
                isMerged[ni][nj] = true
                break
            } else break
        }
        return if (i != ni || j != nj ) Task(i, j, ni, nj, s) else null
    }

    fun Task.applyTask(): Int {
        board[i][j] -= score
        board[ni][nj] += score
        return board[ni][nj]
    }

    fun Task.recoveryTask() {
        board[i][j] += score
        board[ni][nj] -= score
    }

    fun backtracking(moveCount: Int) {
        if (moveCount > 1) return

        val taskList = mutableListOf<Task>()

        for (d in Direction.entries) {
            getAllIdxByDirection(board.size, d) { i, j ->
                generateTask(i, j, d, board[i][j])
                    ?.let {
                        taskList.add(it)
                        val score = it.applyTask()
                        maxScore = maxOf(maxScore, score)
                    }
            }
            isMerged.init()

            println("--- moveCount: ${moveCount}, apply Direction: ${d.name}")
            println(board.joinToString("\n") { it.joinToString(" ") })

            backtracking(moveCount + 1)

            taskList.reversed().forEach { it.recoveryTask() }
            taskList.clear()
        }
    }

    backtracking(1)

    return maxScore
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val board = List(n) { readLine().split(" ").map { it.toInt() }.toIntArray()}
    println(solution(n, board))
}

main()