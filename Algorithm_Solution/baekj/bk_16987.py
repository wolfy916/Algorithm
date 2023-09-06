# 계란으로 계란치기
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 백트랙킹 함수
def dfs(i, v, N):
    global answer
    # 모든 달걀을 손에 들어봤으면 종료
    if i == N:
        answer = max(answer, v)
        return

    # 손에 든 달걀이 깨진 상태면 넘어감
    if eggs[i][0] <= 0:
        dfs(i + 1, v, N)
        return

    flag = False
    # 하나씩 다 깨봄 + 백트랙킹
    for j in range(N):
        if i == j: continue
        if eggs[j][0] <= 0: continue
        flag = True
        s1, s2 = eggs[i][0], eggs[j][0]
        tmp = 0
        eggs[i][0] -= eggs[j][1]
        eggs[j][0] -= eggs[i][1]
        if eggs[i][0] <= 0:
            tmp += 1
        if eggs[j][0] <= 0:
            tmp += 1
        dfs(i + 1, v + tmp, N)
        eggs[i][0], eggs[j][0] = s1, s2

    # 손에 든 달걀로 깨뜨릴 달걀이 없으면 넘어감
    if not flag:
        dfs(i + 1, v, N)

if __name__ == '__main__':
    N = int(input())
    eggs = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    dfs(0, 0, N)
    print(answer)