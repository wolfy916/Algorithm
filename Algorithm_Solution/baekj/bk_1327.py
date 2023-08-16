# 소트 게임
# 리스트 원소를 문자열로 join하여 dict에 key로 사용한 visited
# 정렬을 시행하며 탐색하는 bfs
import sys
from collections import deque as dq

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [1] 데이터 입력
N, K = map(int, input().split())
nums = list(map(int, input().split()))

# [B] 각 경우의 수를 테스트하는 bfs 함수
def bfs():
    global answer
    q = dq([(0, nums[:])])
    while q:
        cnt, cur = q.popleft()
        if cnt != 0 and cur == nums: continue
        if cur == sorted_nums:
            answer = cnt
            return
        for i in range(N - K + 1):
            temp = cur[:]
            if K > 1:
                for j in range(K // 2):
                    temp[i + j], temp[i + K - j - 1] = temp[i + K - j - 1], temp[i + j]
            key = ''.join(map(str, temp))
            if not visited.get(key):
                visited[key] = True
                q.append((cnt + 1, temp))

# [2] 출력부
sorted_nums = sorted(nums)
answer = -1
visited = dict()  # visited
bfs()
print(answer)