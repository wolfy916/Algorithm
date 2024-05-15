# 인사고과

scores = [[2, 2], [1, 4], [3, 2], [3, 2], [2, 1]]


def solution(scores):
    answer = 0
    target_a, target_b = scores[0]
    target_score = target_a + target_b

    # 첫번째 점수에 대해서 내림차순,
    # 첫 번째 점수가 같으면 두 번째 점수에 대해서 오름차순으로 정렬합니다.
    scores.sort(key=lambda x: (-x[0], x[1]))
    maxb = 0

    for a, b in scores:
        if target_a < a and target_b < b:
            return -1

        # b의 정렬은 오름차순이므로 이를 위배하는 b < maxb는
        # 앞쪽에 현재 a보다 더 큰 a가 존재하는 것을 의미
        # -> 같은 a값 내에서 더 큰 b가 앞에 존재할 수 없기 때문
        # 따라서, b < maxb는 걸러짐
        if b >= maxb:
            maxb = b
            if a + b > target_score:
                answer += 1

    return answer + 1