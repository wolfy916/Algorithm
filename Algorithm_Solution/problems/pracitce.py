numbers = [9, 1, 5, 3, 6, 2]

def solution(numbers):
    lenV = len(numbers)
    answer = [0] * lenV
    answer[lenV - 1] = -1
    temp = [numbers[-1]]
    for i in range(lenV - 2, -1, -1):
        while temp[-1] <= numbers[i]:
            temp.pop()
        answer[i] = -1 if temp == [] else temp[-1]
        temp.append(numbers[i])
    return answer

print(solution(numbers))