def solution(play_time, adv_time, logs):
    def chg_second(time):
        time = list(time.split(':'))

        time_for_second = 0
        for i in range(3):
            temp = time[i].lstrip('0')
            if temp:
                time_for_second += int(temp) * 60 ** (2 - i)
        return time_for_second

    def chg_datetime(time):
        hour = time // 3600
        time %= 3600
        minute = time // 60
        second = time % 60
        lst = [hour, minute, second]
        for i in range(3):
            temp_str = str(lst[i])
            if len(temp_str) < 2:
                temp_str = '0' + temp_str
            lst[i] = temp_str
        return ':'.join(lst)

    # 동영상 총 재생시간과 광고고
    play_time = chg_second(play_time)
    adv_time = chg_second(adv_time)

    table = [0] * (play_time + 1)
    for log in logs:  # log = "HH:MM:SS-HH:MM:SS"
        log_s, log_e = chg_second(log[:8]), chg_second(log[9:])
        table[log_s] += 1
        table[log_e] -= 1

    for i in range(1, play_time + 1):
        table[i] += table[i - 1]

    for i in range(1, play_time + 1):
        table[i] += table[i - 1]

    table = [0] + table

    maxV = 0
    result = 0
    for i in range(adv_time, play_time + 2):
        temp = table[i] - table[i - adv_time]
        if maxV < temp:
            maxV = temp
            result = i - adv_time

    answer = chg_datetime(result)

    return answer


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))