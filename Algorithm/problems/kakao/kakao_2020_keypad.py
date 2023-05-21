# 키패드 누르기

input_data = [
    ([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right", "LRLLLRLLRRL"),
    ([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left", "LRLLRRLLLRR"),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right", "LLRLLRLLRL")
]

def distance(si, sj, ei, ej):
    return abs(si-ei) + abs(sj-ej)

def solution(numbers, hand):
    # 키패드 딕셔너리 생성
    keypad = dict()
    for i in range(3):
        for j in range(3):
            keypad[(3*i+j+1)] = (i, j)
    keypad[0] = (3, 1)

    # 왼손, 오른손이 담당하는 숫자들
    left_lst, right_lst = [1, 4, 7], [3, 6, 9]

    # 왼손, 오른손 현재 위치
    li, lj = 3, 0
    ri, rj = 3, 2

    answer = ''
    for num in numbers:
        ni, nj = keypad[num]
        if num in left_lst:
            answer += "L"
            li, lj = ni, nj
        elif num in right_lst:
            answer += "R"
            ri, rj = ni, nj
        else:
            left_d = distance(li, lj, ni, nj)
            right_d = distance(ri, rj, ni, nj)
            if left_d > right_d:
                answer += "R"
                ri, rj = ni, nj
            elif left_d < right_d:
                answer += "L"
                li, lj = ni, nj
            else:
                if hand == "right":
                    answer += "R"
                    ri, rj = ni, nj
                else:
                    answer += "L"
                    li, lj = ni, nj

    return answer


for idx, (numbers, hand, answer) in enumerate(input_data):
    result = solution(numbers, hand)
    print(f'{idx+1}번의 결과--------------------------')
    print(result)
    print("정답") if result == answer else print("오답")
    print('-----------------------------------------')
