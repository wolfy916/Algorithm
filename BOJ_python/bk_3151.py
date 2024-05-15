# 합이 0
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [main]
if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    maxA, minA = max(A), abs(min(A))
    plus = [0] * (maxA + 1)
    minus = [0] * (minA + 1)
    zero = 0
    for a in A:
        if a < 0:
            minus[abs(a)] += 1
        elif a > 0:
            plus[a] += 1
        else:
            zero += 1

    answer = 0
    # case (0, 0, 0)
    if zero > 2:
        answer += zero * (zero - 1) * (zero - 2) // 6

    # case (a, -a, 0)
    for i in range(1, min(maxA, minA) + 1):
        if plus[i] == 0 or minus[i] == 0: continue
        answer += plus[i] * minus[i] * zero

    # case (a, a, c)
    for i in range(1, maxA + 1):
        if plus[i] > 1 and 2 * i <= minA and minus[2 * i] > 0:
            answer += (plus[i] * (plus[i] - 1) // 2) * minus[2 * i]
    for i in range(1, minA + 1):
        if minus[i] > 1 and 2 * i <= maxA and plus[2 * i] > 0:
            answer += (minus[i] * (minus[i] - 1) // 2) * plus[2 * i]

    # case (a, b, c)
    # |a + b| = |c|, c != 0, a + b != c, a != b
    for i in range(1, maxA):
        if plus[i] == 0: continue
        for j in range(i + 1, maxA + 1):
            if plus[j] == 0: continue
            if i + j > minA: continue
            if minus[i + j] == 0: continue
            answer += plus[i] * plus[j] * minus[i + j]
    for i in range(1, minA):
        if minus[i] == 0: continue
        for j in range(i + 1, minA + 1):
            if minus[j] == 0: continue
            if i + j > maxA: continue
            if plus[i + j] == 0: continue
            answer += minus[i] * minus[j] * plus[i + j]

    print(answer)