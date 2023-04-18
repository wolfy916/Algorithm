# 좋다
import sys
input = sys.stdin.readline

def Search(left, right, num):
    while left < right:
        value = temp[left] + temp[right]  # 합 계산
        if value == num:
            return 1
        # 합이 검사 대상 숫자보다 크면 right를 줄임
        elif value > num:
            right -= 1
        # 합이 검사 대상 숫자보다 작으면 left를 늘림
        else:
            left += 1
    return 0

N = int(input())
nums = sorted(list(map(int, input().split())))  # 오름차순 정렬
result = 0
for i in range(N):
    num = nums[i]  # 숫자 하나 선택
    temp = nums[:i] + nums[i+1:]  # 해당 숫자를 제외한 배열을 만듦
    result += Search(0, N-2, num)

print(result)