'''
2024 카카오 테크 인턴십 2번문제
분류 :
'''

def solution(edges):
    maxNode = max(map(lambda x: max(x), edges))
    adjL = [[] for _ in range(maxNode + 1)]
    rec_edges = [[] for _ in range(maxNode + 1)]

    for a, b in edges:
        adjL[a].append(b)
        rec_edges[b].append(a)

    start = 0
    for i in range(maxNode + 1):
        if len(adjL[i]) > 1 and not len(rec_edges[i]):
            start = i
            break

    answer = [start, 0, 0, 0]
    visited = [False] * (maxNode + 1)
    visited[start] = True
    for v in adjL[start]:
        while not visited[v]:
            visited[v] = True
            if 1 < len(adjL[v]):
                answer[3] += 1
                break
            if len(adjL[v]) < 1:
                answer[2] += 1
                break
            w = adjL[v][0]
            if visited[w]: continue
            v = w
        else:
            answer[1] += 1

    return answer

edgess = [
    [[2, 3], [4, 3], [1, 1], [2, 1]],
    [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]],
]
correct = [
    [2, 1, 1, 0],
    [4, 0, 1, 2],
]

if __name__ == '__main__':
    for i in range(2):
        print('------case', i+1)
        answer = solution(edgess[i])
        print('나의 답: ', answer)
        print('정답: ', correct[i])