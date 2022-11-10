# 월드컵
lst = [list(map(int, input().split())) for _ in '_'*4]

# 무승부의 총 합계가 짝수이면 테스트 통과
# def check_tie(result):
#     sum_tie = 0
#     for i in range(1, 18, 3):
#         sum_tie += result[i]
#
#     if sum_tie % 2:
#         return False
#     return True


# 각 팀의 (승, 무, 패) 합산이 5이면 테스트 통과
# def check_sum(result):
#     for i in range(0, 18, 3):
#         sumV = 0
#         for j in range(i, i+3):
#             sumV += result[j]
#         if sumV != 5:
#             return False
#     return True


# 총 승리수와 총 패배수가 같으면 테스트 통과
# def check_wins_loses(result):
#     sum_wins = 0
#     sum_loses = 0
#     for i in range(18):
#         if i % 3 == 0:
#             sum_wins += result[i]
#             continue
#         if i % 3 == 2:
#             sum_loses += result[i]
#     if sum_wins == sum_loses:
#         return True
#     return False


def check(result):
    sum_wins = sum_tie = sum_loses = 0   # 총 승리, 총 무승부, 총 패배
    sum_team_log = 0  # 각 팀의 (승,무,패)의 합
    cnt_tie = 0  # 무승부가 있는 팀의 수
    for i in range(18):
        if i % 3 == 0:
            sum_wins += result[i]
            sum_team_log = result[i]
        elif i % 3 == 1:
            sum_tie += result[i]
            if result[i]:
                cnt_tie += 1
            sum_team_log += result[i]
        elif i % 3 == 2:
            sum_loses += result[i]
            sum_team_log += result[i]
            # 각 팀의 (승,무,패)의 합이 5가 아니면 False
            if sum_team_log != 5:
                return 0
    # 총 승리수가 총 패배수와 같지 않으면 False
    if sum_wins != sum_loses:
        return 0
    # 총 승리, 패배, 무승부 합산이 30이 아니면 False
    if sum_wins + sum_loses + sum_tie != 30:
        return 0
    # 총 무승부 수가 홀수이면 False
    if sum_tie % 2:
        return 0
    # 무승부가 있는 팀의 수가 홀수이면 False
    if cnt_tie % 2:
        return 0
    # 테스트 모두 통과하면 True
    return 1


for line in lst:
    print(check(line), end=' ')

print(check([2, 1, 2]*18))