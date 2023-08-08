from collections import deque as dq

def solution(program):
    program.sort(key=lambda x:[x[1], -x[0]])
    ans = [0] * 11
    ans[0] = program[0][1]
    stack = dq([program.pop(0)])
    while stack[-1][1] == program[0][1]:
        stack.append(program.pop(0))
        ans[0] = stack[-1][1]
    while stack:
        prior, start, time = stack.pop()
        ans[prior] += ans[0] - start
        ans[0] += time
        while program:
            if start <= program[0][1] <= ans[0]:
                if stack:
                    if stack[-1][0] <= program[0][0]: break
                stack.append(program.pop(0))
            else:
                break
    return ans

print(solution([[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]))