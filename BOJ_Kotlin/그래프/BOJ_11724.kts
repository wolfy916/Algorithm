// 연결 요소의 개수
// 분류 : 그래프, DFS

fun solution(n: Int, arr: Array<List<Int>>): Int {
    val adjL = Array(n + 1) { mutableListOf<Int>() }

    for ((a, b) in arr) {
        adjL[a].add(b)
        adjL[b].add(a)
    }

    var answer = 0
    val visited = Array(n + 1) { false }

    fun dfs(v: Int) {
        visited[v] = true
        for (w in adjL[v]) {
            if (visited[w]) continue
            dfs(w)
        }
    }

    for (i in 1 until n + 1) {
        if (visited[i]) continue
        answer++
        dfs(i)
    }

    return answer
}

fun main() = with(System.`in`.bufferedReader()) {
    val (n, m) = readLine().split(" ").map{ it.toInt() }
    val arr = Array(m) { readLine().split(" ").map{ it.toInt() } }

    print(solution(n, arr))
}

main()