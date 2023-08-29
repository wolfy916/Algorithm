# 0 만들기
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 선택한 수식기호를 대입하여 계산하는 함수
def calculate(select, N):
    # [B-1] 공백부터 적용
    nums = [1]
    for i in range(N - 1):
        k = select[i]
        if k == 2:
            nums.append(nums.pop() * 10 + i + 2)
        else:
            nums.append(i + 2)

    # [B-2] 계산 값이 0인지 확인
    v = nums.pop(0)
    for k in select:
        if k == 2:
            continue
        elif k == 1:
            v -= nums.pop(0)
        else:
            v += nums.pop(0)

    return v == 0


# [C] dfs 완전탐색
def dfs(cnt, N, select):
    if cnt == N - 1:
        if calculate(select, N):
            eqn = '1'
            for i in range(N - 1):
                eqn += sign[select[i]] + str(i+2)
            answer.append(eqn)
        return
    for k in range(3):
        dfs(cnt + 1, N, select + [k])

# [D] solution
def solution(N):
    global answer, sign
    answer = []
    sign = ['+', '-', ' ']
    dfs(0, N, [])
    return sorted(answer)

# [main]
if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        N = int(input())
        for eqn in solution(N):
            print(eqn)
        print()