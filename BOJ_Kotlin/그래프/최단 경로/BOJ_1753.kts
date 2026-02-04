import java.util.PriorityQueue

/**
 * 최단 경로
 * 골드 4
 * 다이크스트라
 * */

fun solution(v: Int, k: Int, edges: List<List<Int>>): String {
    // 1. 인접리스트 생성
    val adjList = List(v + 1) { mutableListOf<Pair<Int, Int>>() }

    // 2. 인접리스트에 간선 기록
    edges.forEach {
        val (u, v, w) = it
        adjList[u].add(v to w) // 단방향 기록
    }

    // 3. 다이크스트라 세팅
    val pq = PriorityQueue<Pair<Int, Int>>(compareBy { it.second })
    val minPrice = IntArray(v + 1) { Int.MAX_VALUE }
    val visited = BooleanArray(v + 1) { false }

    pq.add(k to 0)
    minPrice[k] = 0 // 시작점의 비용은 0

    // 4. 다이크스트라 로직 실행
    while (pq.isNotEmpty()) {
        val (cur, _) = pq.poll()

        if (visited[cur]) continue
        visited[cur] = true

        for ((next, nextCost) in adjList[cur]) {
            if (minPrice[next] > minPrice[cur] + nextCost) {
                minPrice[next] = minPrice[cur] + nextCost
                pq.add(next to minPrice[next])
            }
        }
    }

    // 5. 결과 출력
    val result = mutableListOf<String>()
    val inf = "INF"
    for (i in 1..v) {
        val price = minPrice[i]
        if (price < Int.MAX_VALUE) {
            result.add(price.toString())
        } else {
            result.add(inf)
        }
    }

    return result.joinToString("\n")
}

fun main() = with(System.`in`.bufferedReader()) {
    fun readIntList() = readLine().split(" ").map { it.toInt() }
    val (v, e) = readIntList()
    val k = readLine().toInt()
    val edges = List(e) { readIntList() }
    println(solution(v, k, edges))
}

main()