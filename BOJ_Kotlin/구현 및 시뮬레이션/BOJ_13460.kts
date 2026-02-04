import kotlin.math.abs

/**
 * 구슬 탈출 2
 * 골드 1
 * 구현, 백트랙킹
 * */

enum class Direction(val di: Int, val dj: Int) {
    UP(-1, 0),
    DOWN(1, 0),
    LEFT(0, -1),
    RIGHT(0, 1);
}

enum class Color { RED, BLUE }

fun getPriority(d: Direction, ri:Int, rj:Int, bi:Int, bj:Int): Color {
    var r:Int; var b:Int
    when (d) {
        Direction.UP -> {
            r = abs(0 - ri)
            b = abs(0 - bi)
        }
        Direction.DOWN -> {
            r = abs(10 - ri)
            b = abs(10 - bi)
        }
        Direction.LEFT -> {
            r = abs(0 - rj)
            b = abs(0 - bj)
        }
        Direction.RIGHT -> {
            r = abs(10 - rj)
            b = abs(10 - bj)
        }
    }
    return if (r <= b) Color.RED else Color.BLUE
}

fun solution(board: List<CharArray>): Int {
    var ri = 0; var rj = 0
    var bi = 0; var bj = 0

    board.forEachIndexed { i, charArray ->
        charArray.forEachIndexed { j, char ->
            when (char) {
                'R' -> {
                    ri = i
                    rj = j
                }
                'B' -> {
                    bi = i
                    bj = j
                }
                else -> Unit
            }
        }
    }

    fun getNextCoordinate(d: Direction, i:Int, j:Int): Triple<Int, Int, Boolean> {
        var ni = i; var nj = j; var isGoal = false
        fun isContinue() =
            when (board[ni + d.di][nj + d.dj]) {
                '.' -> true
                'O' -> {
                    isGoal = true
                    true
                }
                else -> false
            }
        while (isContinue()) {
            ni += d.di
            nj += d.dj
            if (isGoal) break
        }
        return Triple(ni, nj, isGoal)
    }

    fun exchange(i: Int, j: Int, ni: Int, nj: Int) {
        val tempChar = board[ni][nj]
        board[ni][nj] = board[i][j]
        board[i][j] = tempChar
    }

    var result = 11

    fun search(count: Int, ri: Int, rj: Int, bi: Int, bj: Int) {
        if (count >= result) return
        for (d in Direction.entries) {
            val p = getPriority(d, ri, rj, bi, bj)
            var nr: Triple<Int, Int, Boolean>; var nb: Triple<Int, Int, Boolean>
            when (p) {
                Color.RED -> {
                    nr = getNextCoordinate(d, ri, rj)
                    if (nr.third) board[ri][rj] = '.'
                    else exchange(ri, rj, nr.first, nr.second)
                    nb = getNextCoordinate(d, bi, bj)
                    if (nb.third) board[bi][bj] = '.'
                    else exchange(bi, bj, nb.first, nb.second)
                }
                Color.BLUE -> {
                    nb = getNextCoordinate(d, bi, bj)
                    if (nb.third) board[bi][bj] = '.'
                    else exchange(bi, bj, nb.first, nb.second)
                    nr = getNextCoordinate(d, ri, rj)
                    if (nr.third) board[ri][rj] = '.'
                    else exchange(ri, rj, nr.first, nr.second)
                }
            }
            when {
                nr.third && nb.third.not() -> result = count + 1
                nr.third.not() && nb.third.not() -> {
                    if (ri != nr.first || rj != nr.second || bi != nb.first || bj != nb.second) {
                        search(count + 1, nr.first, nr.second, nb.first, nb.second)
                    } else continue
                }
            }
            when (p) {
                Color.RED -> {
                    if (nb.third) board[bi][bj] = 'B'
                    else exchange(bi, bj, nb.first, nb.second)
                    if (nr.third) board[ri][rj] = 'R'
                    else exchange(ri, rj, nr.first, nr.second)
                }
                Color.BLUE -> {
                    if (nr.third) board[ri][rj] = 'R'
                    else exchange(ri, rj, nr.first, nr.second)
                    if (nb.third) board[bi][bj] = 'B'
                    else exchange(bi, bj, nb.first, nb.second)
                }
            }

            if (result == count + 1) return
        }
    }

    search(0, ri, rj, bi, bj)

    return if (result <= 10) result else -1
}

fun main() = with(System.`in`.bufferedReader()) {
    val (n, _) = readLine().split(" ").map { it.toInt() }
    val board = List(n) { readLine().toCharArray() }
    println(solution(board))
}

main()