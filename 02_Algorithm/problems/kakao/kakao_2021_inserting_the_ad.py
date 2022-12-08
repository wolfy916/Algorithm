# 카카오 2021 블라인드 채용 기출 문제
# Lv. 3 광고 삽입

'''
# play_time, adv_time
길이 8로 고정된 HH:MM:SS 형식이며, 00:00:01 ~ 99:59:59 이하
adv_time <= play_time
'''

'''
# logs
1 ~ 300,000 길이를 갖는 리스트
각 원소는 길이 17로 고정된 문자열 'HH:MM:SS~HH:MM:SS'
'''

play_time = "99:59:59"
adv_time = "25:00:00"
logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]


# HH:MM:SS -> S
def chg_second(time):
    time = list(time.split(':'))
    time_for_second = 0
    for i in range(3):
        temp = time[i].lstrip('0')
        if temp:
            time_for_second += int(temp) * 60 ** (2-i)
    return time_for_second


# S -> HH:MM:SS
def chg_datetime(time):
    hour = time // 3600
    time %= 3600
    minute = time // 60
    second = time % 60
    lst = [hour, minute, second]
    for i in range(3):
        temp_str = str(time[i])
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
    table[log_e+1] -= 1

for i in range(1, play_time + 1):
    table[i] += table[i-1]

for i in range(1, play_time + 1):
    table[i] += table[i-1]

table = [0] + table

maxV = 0
result = 0
for i in range(adv_time, play_time+2):
    temp = table[i] - table[i-adv_time]
    if maxV < temp:
        maxV = temp
        result = i - adv_time

answer = chg_datetime(result)
print(answer)