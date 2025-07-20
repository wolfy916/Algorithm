/**
 * 예산
 * 실버 2
 * 이분 탐색
 * */

import kotlin.math.max

fun solution(countArea: Int, budgets: List<Int>, totalBudget: Int): Int {
    // 예산 리스트를 정렬
    val sortedBudgets = budgets.sorted()

    // [A] 예상치 v로 소모될 총 예산을 계산하는 함수
    fun simulate(v: Int): Int {
        var sumV = 0
        for (idx in sortedBudgets.indices) {
            // [A-1] 예상치 이하의 예산은 그대로 합산
            if (sortedBudgets[idx] <= v) {
                sumV += sortedBudgets[idx]
            // [A-2] 예상치보다 클 경우, 나머지 값은 모두 예상치로 합산
            } else {
                sumV += v * (countArea - idx)
                break
            }
        }
        return sumV
    }

    // [1] 세팅
    var answer = 0
    var left = 1
    var right = sortedBudgets.last() // answer는 최대값보다 클 수 없다.

    // [2] 이분탐색 실행
    while (left <= right) {
        val mid = (left + right) / 2
        val usedTotalBudget = simulate(mid)
        // [2-1] simulate 값이 총 예산 이하이면 정답 후보이므로 answer 갱신
        if (usedTotalBudget <= totalBudget) {
            left = mid + 1
            answer = max(answer, mid)
        } else {
            right = mid - 1
        }
    }

    return answer
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val list = readLine().split(" ").map{ it.toInt() }
    val m = readLine().toInt()

    val answer = solution(n, list, m)

    print(answer)
}

main()