stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
# greedy
def solution(stones, k):
    n = len(stones)  # 징검다리 길이
    answer = 0
    i = 0
    while i <= n-k:
        maxV = maxIdx = 0
        for j in range(i, i+k):
            if maxV <= stones[j]:
                maxV = stones[j]
                maxIdx = j
        if maxV:
            if answer:
                answer = min(answer, maxV)
            else:
                answer = maxV
        i = maxIdx + 1
    return answer

# deque
# from collections import deque
#
# def solution(stones, k):
#     answer = 2*(10**8)
#     deq = deque([])
#     lenV = 0
#     for i, stone in enumerate(stones):
#         if lenV:
#             for j in range(lenV-1, -1, -1):
#                 if deq[j][1] < stone:
#                     deq.pop()
#                     lenV -= 1
#                 else:
#                     break
#         deq.append((i, stone))
#         lenV += 1
#         if deq[0][0] < i-k+1:
#             deq.popleft()
#             lenV -= 1
#         if i >= k-1:
#             answer = min(answer, deq[0][1])
#     return answer

print(solution(stones, k))
