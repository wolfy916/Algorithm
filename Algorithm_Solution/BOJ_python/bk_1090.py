'''
체커 - 백준 플래티넘 4
분류 : 완전탐색?..
'''
import sys

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [main]
if __name__ == '__main__':
    N = int(input())
    chks = [tuple(map(int, input().split())) for _ in range(N)]

    # 각 개수(인덱스)마다 최소거리를 저장하기 위해 큰값으로 초기화
    ans = [float('inf')] * (N + 1)

    for i in range(N):
        for j in range(N):
            # 모든 점의 좌표를 설정
            x, y = chks[i][0], chks[j][1]

            # 한점에서 부터 모든 점까지의 거리를 저장
            distance = []
            for h in range(N):
                distance.append(abs(x - chks[h][0]) + abs(y - chks[h][1]))
            distance.sort()

            sumV = 0
            for dist in range(N):
                sumV += distance[dist]
                if ans[dist + 1] > sumV:
                    ans[dist + 1] = sumV

    print(*ans[1:])