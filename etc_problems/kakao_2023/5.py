'''
2024 카카오 테크 인턴십 5번문제
분류 :
'''
def solution(n, tops):
    DP = [0] * 2 * (n + 1)
    DP[0] = 1
    DP[1] = 1
    if tops[0] == 1:
        DP[2] = 3
        DP[3] = 4
    else:
        DP[2] = 2
        DP[3] = 3
    for i in range(2, n + 1):
        p = i
        q = i + 1
        if tops[i - 1] == 0:
            DP[p] = DP[p - 1] + DP[p - 2]
            DP[q] = DP[q - 1] + DP[q - 2]
        else:
            DP[p] = 2 * DP[p - 1] + DP[p - 2]
            DP[q] = DP[p] + DP[p - 1]
        DP[p] %= 10007
        DP[q] %= 10007
    return


n = [4, 2, 10]
tops = [
    [1, 1, 0, 1],
    [0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
correct = [149, 11, 7704]

if __name__ == '__main__':
    for i in range(3):
        print(solution(n, tops))