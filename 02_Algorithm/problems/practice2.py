# stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
stones = [6, 5, 1, 6, 2, 1]
# k = 3
k = 3
def solution(stones, k):
    n = len(stones)  # 징검다리 길이
    left, right = 1, 2*(10**8)  # left, right

    # 인덱스 0이상 k미만 돌 중 하나를 건널 수 있을 때까지 mid 계산
    first = max(stones[:k])
    mid = (left + right) // 2
    while mid > first:
        right = mid - 1
        mid = (left + right) // 2

    while left <= right:
        mid = (left + right) // 2
        q = list(range(k))
        flag = False
        while q:
            v = q.pop(0)
            if v + k - 1 >= n:
                flag = True
                break
            else:
                for w in range(v+1, v+k):
                    if w not in q and stones[w] >= mid:
                        q.append(w)
        if flag:
            left = mid + 1
        else:
            right = mid - 1

    return mid

print(solution(stones, k))