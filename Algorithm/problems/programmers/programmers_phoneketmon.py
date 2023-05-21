
# 1
nums = [3,1,2,3]

# 2
# nums = [3,3,3,2,2,4]

# 3
# nums = [3,3,3,2,2,2]

def solution(nums):
    answer = 0
    lst = []
    for num in nums:
        if num not in lst:
            lst.append(num)
            answer += 1
    lenV = len(nums) // 2
    if answer > lenV:
        answer = lenV
    return answer

print(solution(nums))