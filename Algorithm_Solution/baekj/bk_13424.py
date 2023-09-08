# 비밀 모임
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 메인 로직 함수
def solution():
    # 인접 행렬 초기화
    INF = float('inf')
    adjM = [[INF] * (N + 1) for _ in range(N + 1)]
    # 자기 자신을 향한 경로 가중치 0 초기화
    for i in range(1, N + 1):
        adjM[i][i] = 0
    # 양방향 간선 기록
    for a, b, c in edges:
        adjM[a][b] = c
        adjM[b][a] = c
    # 플로이드 워셜 : a -> b와 a -> r -> b의 경로 가중치를 비교하여 최소값으로 갱신
    for r in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                adjM[a][b] = min(adjM[a][b], adjM[a][r] + adjM[r][b])
    # 방 번호를 순회하며, 모든 사람들의 총 이동거리가 최소가 되는 방번호 탐색
    minV = INF
    answer = 0
    for i in range(1, N + 1):
        sumV = sum(map(lambda x: adjM[x][i], rooms))
        if minV > sumV:
            answer = i
            minV = sumV

    return answer

# [main]
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        edges = [tuple(map(int, input().split())) for _ in range(M)]
        K = int(input())
        rooms = tuple(map(int, input().split()))
        print(solution())
