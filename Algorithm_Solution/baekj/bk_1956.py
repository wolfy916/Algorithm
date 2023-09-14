# 운동
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [main]
if __name__ == '__main__':
    V, E = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(E)]

    # [1] 인접 행렬 INF값으로 초기화
    INF = float('inf')
    adjM = [[INF] * (V + 1) for _ in range(V + 1)]

    # [2] 단방향 간선의 가중치 기록
    for a, b, c in edges:
        adjM[a][b] = c

    # [3] 플로이드 워셜
    # s -> e : 직진 경로
    # s -> r -> e : 노드 r을 경유하는 경로
    # 두 경로의 합산 가중치를 비교하여 작은 값으로 갱신
    for r in range(1, V + 1):
        for s in range(1, V + 1):
            for e in range(1, V + 1):
                adjM[s][e] = min(adjM[s][e], adjM[s][r] + adjM[r][e])

    # [4] 자기 자신에게 되돌아오는 순환 경로의 가중치로 answer 갱신
    answer = float('inf')
    for i in range(1, V + 1):
        answer = min(answer, adjM[i][i])

    print(answer if answer < INF else -1)