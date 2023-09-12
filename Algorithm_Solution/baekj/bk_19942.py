# 다이어트
import sys

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] dfs 백트랙킹
# state : 현재 합산 영양소 상태
# price : 현재 합산 가격
# select : 현재까지 선택하 식재료 인덱스 리스트
def dfs(state, price, select):
    global selected, minV, answer
    # 4가지 영양소 만족 여부 확인
    for k in range(4):
        if state[k] < m[k]: break
    else:
        # 영양소 만족시 가격 최솟값으로 갱신하고 선택한 식재료 리스트도 저장
        if price < minV:
            minV = price
            answer = select[:]

    s = select[-1] if select else 0
    for i in range(s, N):
        # 선택할 식재료의 가격을 더했을때 갱신된 minV 값 이상이라면 거름
        if price + nutrients[i][4] >= minV: continue
        select.append(i + 1)
        for k in range(4):
            state[k] += nutrients[i][k]
        dfs(state, price + nutrients[i][4], select)
        select.pop()
        for k in range(4):
            state[k] -= nutrients[i][k]

# [C] 메인 로직 함수
def solution(N):
    global selected, minV, answer
    minV = float('inf')
    answer = []
    dfs([0, 0, 0, 0], 0, [])
    if minV == float('inf'):
        print(-1)
        print()
    else:
        print(minV)
        print(*answer)

# [main]
if __name__ == '__main__':
    N = int(input())
    m = tuple(map(int, input().split()))
    nutrients = [tuple(map(int, input().split()))for _ in range(N)]
    solution(N)