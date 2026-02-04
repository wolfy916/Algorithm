/**
 * 주사위 굴리기
 * 골드 4
 * 구현
 * */

enum class Direction(val value: Int, val i: Int, val j: Int) {
    EAST(1, 0, 1),
    WEST(2, 0, -1),
    NORTH(3, -1, 0),
    SOUTH(4, 1, 0);

    companion object {
        operator fun invoke(value: Int): Direction? =
            Direction.entries.find { it.value == value }
    }
}

class Dice {
    private val verticalAxis = MutableList(4) { 0 } // 2, 1, 5, 6
    private val horizontalAxis = MutableList(4) { 0 } // 4, 1, 3, 6

    val getTopSideValue get() = verticalAxis[1]
    val getBottomSideValue get() = verticalAxis[3]

    fun setBottomSideValue(value: Int) {
        verticalAxis[3] = value
        horizontalAxis[3] = value
    }

    fun rollDice(d: Direction) {
        when (d) {
            Direction.EAST -> {
                rightShift(horizontalAxis)
                horizontalAxis.synchronizeTo(verticalAxis)
            }
            Direction.WEST -> {
                leftShift(horizontalAxis)
                horizontalAxis.synchronizeTo(verticalAxis)
            }
            Direction.NORTH -> {
                leftShift(verticalAxis)
                verticalAxis.synchronizeTo(horizontalAxis)
            }
            Direction.SOUTH -> {
                rightShift(verticalAxis)
                verticalAxis.synchronizeTo(horizontalAxis)
            }
        }
    }

    private fun leftShift(axis: MutableList<Int>) {
        axis.add(axis.removeFirst())
    }

    private fun rightShift(axis: MutableList<Int>) {
        axis.add(0, axis.removeLast())
    }

    private fun MutableList<Int>.synchronizeTo(subAxis: MutableList<Int>) {
        subAxis[1] = this[1]
        subAxis[3] = this[3]
    }
}

fun solution(
    n: Int, m: Int,
    x: Int, y: Int, k: Int,
    board: List<IntArray>,
    order: List<Int>
): String {
    val result = mutableListOf<Int>()
    val dice = Dice()
    var i = x; var j = y;

    fun isValid(i: Int, j: Int) = 0 <= i && i < n && 0 <= j && j < m

    order.forEach { v ->
        val d = Direction(v) ?: throw Exception("unknown direction value")
        val ni = i + d.i; val nj = j + d.j
        if (isValid(ni, nj)) {
            dice.rollDice(d)
            when(board[ni][nj]) {
                0 -> {
                    board[ni][nj] = dice.getBottomSideValue
                }
                else -> {
                    dice.setBottomSideValue(board[ni][nj])
                    board[ni][nj] = 0
                }
            }
            result.add(dice.getTopSideValue)
            i = ni; j = nj;
        }
    }

    return result.joinToString("\n")
}

fun main() = with(System.`in`.bufferedReader()) {
    val (n, m, x, y, k) = readLine().split(" ").map { it.toInt() }
    val board = List(n) { readLine().split(" ").map { it.toInt() }.toIntArray() }
    val order = readLine().split(" ").map { it.toInt() }
    println(solution(n, m, x, y, k, board, order))
}

main()