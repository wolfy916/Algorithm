def BinarySearch(s, e, m, c, d):  # s : 시작점 인덱스, e : 끝점 인덱스, m : 중간값 인덱스, c : 남은 횟수
    if c == 0:
        return d

    left_distance = houses[m] - houses[s]
    right_distance = houses[e] - houses[m]

    if left_distance < right_distance:
        return BinarySearch(m, e, (m + e) // 2, c - 1, left_distance)
    elif left_distance > right_distance:
        return BinarySearch(s, m, (s + m) // 2, c - 1, right_distance)
    else:
        a = BinarySearch(m, e, (m + e) // 2, c - 1, left_distance)
        b = BinarySearch(s, m, (s + m) // 2, c - 1, right_distance)
        if a >= b:
            return b
        else:
            return a


N, C = map(int, input().split())
houses = [int(input()) for house in range(N)]
houses.sort()

if C > 2:
    if N % 2:
        maxV = BinarySearch(0, N - 1, (N - 1) // 2, C - 2, N)
    else:
        maxV1 = BinarySearch(0, N - 1, (N - 1) // 2, C - 2, N)
        maxV2 = BinarySearch(0, N - 1, ((N - 1) // 2) + 1, C - 2, N)
        if maxV1 >= maxV2:
            maxV = maxV1
        else:
            maxV = maxV2
else:
    maxV = houses[-1] - houses[0]

print(maxV)