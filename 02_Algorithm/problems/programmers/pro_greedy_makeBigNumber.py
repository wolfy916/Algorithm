# 큰 수 만들기
number = "4321"
k = 3

def solution(number, k):
    number = list(map(int, number))
    stack = [number[0]]
    cnt = 0
    for i in range(1, len(number)):
        while cnt < k and stack and stack[-1] < number[i]:
            stack.pop()
            cnt += 1
        stack.append(number[i])
    for _ in range(k - cnt):
        stack.pop()
    return ''.join(map(str, stack))

print(solution(number, k))