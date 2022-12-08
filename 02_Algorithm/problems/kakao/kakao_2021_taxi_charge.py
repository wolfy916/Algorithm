# 2021 KAKAO BLIND RECRUITMENT 합승 택시 요금

# 1번 입력
# n = 6
# s = 4
# a = 6
# b = 2
# fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
# result = 82

# 2번 입력
# n = 7
# s = 3
# a = 4
# b = 1
# fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
# result = 14

# 3번 입력
# n = 6
# s = 4
# a = 5
# b = 6
# fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
# result = 18


def solution(n, s, a, b, fares):

    def taxi_bfs(start, end, n, visited_lst):
        if start == end:
            return 0, []
        visited = [0] * (n+1)
        visited[start] = -1
        for to_visited in visited_lst:
            visited[to_visited] = -1
        minV = 100000 * (n-1) + 1
        minV_path = []
        # q = [(start, 0)]
        q = [(start, [start], 0)]
        while q:
            v, path, charge = q.pop(0)
            if v == end:
                if minV > charge:
                    minV = charge
                    minV_path = path
            else:
                for w in range(1, n+1):
                    w_charge = adjM[v][w]
                    if w_charge and (visited[w] == 0 or charge + w_charge <= visited[w]):
                        visited[w] = charge + w_charge
                        # q.append((w, visited[w]))
                        q.append((w, path+[w], visited[w]))
        # return minV
        return minV, minV_path

    adjM = [[0] * (n + 1) for _ in '_' * (n + 1)]
    for n1, n2, v in fares:
        adjM[n1][n2] = v
        adjM[n2][n1] = v

    answer = 100001 * (n-1)
    for i in range(1, n+1):
        two_charge, two_visited = taxi_bfs(s, i, n, [])
        a_charge, a_path = taxi_bfs(i, a, n, two_visited)
        b_charge, b_path = taxi_bfs(i, b, n, two_visited)
        answer = min(answer, two_charge + a_charge + b_charge)

    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
))