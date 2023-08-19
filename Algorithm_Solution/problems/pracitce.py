def solution(gems):
    # [1] 각 보석에 대한 사용 여부 리스트 생성
    gem_type = set(gems)  # 보석 종류
    gem_lst = list(gem_type)
    del gem_type
    N, M = len(gems), len(gem_lst)  # 전체 길이, 보석 종류 개수
    ref = {gem_lst[i]: i for i in range(M)}
    used = [0] * M

    # [2] 투 포인터
    p1 = p2 = 0
    min_length = N
    answer = [1, N]
    cnt = 0
    while p1 < N or p2 < N:
        # [2-1] 탐색 구간이 모든 보석 종류를 모을 때까지 p2 이동
        while p2 < N and cnt < M:
            used[ref[gems[p2]]] += 1
            if used[ref[gems[p2]]] == 1:
                cnt += 1
            p2 += 1

        # [2-2] 모든 보석 종류를 모았으며, 기준값 보다 구간의 길이가 작다면 갱신
        if cnt >= M and min_length > p2 - p1:
            min_length = p2 - p1
            answer = [p1 + 1, p2]

        # [2-3] 좌측 포인터인 p1을 1만큼 이동
        used[ref[gems[p1]]] -= 1
        if used[ref[gems[p1]]] == 0:
            cnt -= 1
        p1 += 1

    return answer

Gems = [
    ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],
    ["AA", "AB", "AC", "AA", "AC"],
    ["XYZ", "XYZ", "XYZ"],
    ["ZZZ", "YYY", "NNNN", "YYY", "BBB"],
    ["A", "B", "B", "C", "B", "B", "B", "B", "C", "A"],
]

for i in range(5):
    print(f"#{i+1} {solution(Gems[i])}")

#1 [3, 7]
#2 [1, 3]
#3 [1, 1]
#4 [1, 5]