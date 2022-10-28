A = "99:59:59"


def change_for_second(time):
    time = list(time.split(':'))
    time_for_second = 0
    for i in range(3):
        time_for_second += int(time[i].lstrip('0')) * 60 ** (2-i)
    return time_for_second

A = change_for_second(A)
print(A)