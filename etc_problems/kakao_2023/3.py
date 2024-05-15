'''
2024 카카오 테크 인턴십 3번문제
분류 :
'''

# 야매 풀이
# def solution(dice):
#     n = len(dice)
#     nums = list(range(1, n + 1))
#     nums.sort(key=lambda x: [sum(dice[x - 1]), max(dice[x - 1])])
#     return sorted(nums[n // 2:])

def solution(dice):
    return

dices = [
    [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]],
    [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]],
    [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]],
]

correct = [
    [1, 4],
    [2],
    [1, 3],
]

if __name__ == '__main__':
    for i in range(3):
        answer = solution(dices[i])
        print('------case', i+1)
        print('나의 답: ', answer)
        print('정답: ', correct[i])