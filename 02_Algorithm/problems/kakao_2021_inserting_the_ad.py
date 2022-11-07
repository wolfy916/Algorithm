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


# 시간을 초 단위로 반환
def change(time):
    time = list(time.split(':'))
    time_for_second = 0
    for i in range(3):
        temp = time[i].lstrip('0')
        if temp:
            time_for_second += int(temp) * 60 ** (2-i)
    return time_for_second


play_time = change(play_time)
table = [0] * 360002
adv_time = change(adv_time) + 1

for i in range(len(logs)):
    table[change(logs[i][:8])] += 1
    table[change(logs[i][9:]) + 1] -= 1

for i in range(1, play_time + 1):
    table[i] += table[i-1]
print(table)
for i in range(1, play_time + 1):
    table[i] += table[i-1]
print(table)

maxV = 0
result = 0
for i in range(adv_time, play_time + 1):
    temp = table[i] - table[i-adv_time]
    if maxV < temp:
        maxV = temp
        result = i - adv_time
print(maxV)

hour = result // 3600
result -= hour * 3600
minute = result // 60
second = result - minute * 60

time = [hour, minute, second]
for i in range(3):
    temp = str(time[i])
    if len(temp) < 2:
        temp = '0' + temp
    time[i] = temp

answer = ':'.join(time)
print(answer)