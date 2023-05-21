id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

def solution(id_list, report, k):
    user_total = len(id_list)
    report_total = len(report)
    reported_cnt_list = [0] * user_total
    done = [[0]*user_total for _ in '_'*user_total]
    answer = [0] * user_total
    for i in range(report_total):
        user, reported_user = report[i].split()
        user_idx = id_list.index(user)
        reported_user_idx = id_list.index(reported_user)
        if not done[user_idx][reported_user_idx]:
            done[user_idx][reported_user_idx] = 1
            reported_cnt_list[reported_user_idx] += 1
    for i in range(user_total):
        if reported_cnt_list[i] >= k:
            for j in range(user_total):
                if done[j][i]:
                    answer[j] += 1
    return answer

print(solution(id_list, report, k))