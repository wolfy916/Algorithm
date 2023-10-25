# "HH:MM" => M 변환 함수
def trans1(t):
    h, m = t.split(':')
    if h[0] == '0': h = h[1]
    if m[0] == '0': m = m[1]
    return int(h) * 60 + int(m)

# M => "HH:MM" 변환 함수
def trans2(t):
    h, m = divmod(t, 60)
    h = '0' + str(h) if h < 10 else str(h)
    m = '0' + str(m) if m < 10 else str(m)
    return h + ':' + m

def solution(n, t, m, timetable):
    table = sorted(list(map(trans1, timetable)), reverse=True)
    time = 540 - t
    answer = 0
    for _ in range(n):
        time += t
        board = last = 0
        while table and table[-1] <= time and board < m:
            board += 1
            last = table.pop()
        if board < m:
            answer = time
        else:
            answer = last - 1

    return trans2(answer)

print(solution(2,10,2,["09:10", "09:09", "08:00"]))