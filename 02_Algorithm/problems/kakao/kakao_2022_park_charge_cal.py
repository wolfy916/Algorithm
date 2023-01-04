# 주차 요금 계산

# fee = [180, 5000, 10, 600]
# records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

fee = [1, 461, 1, 10]
records = ["00:00 1234 IN"]

def solution(fee, records):
    def h_to_m(t):
        h, m = t.split(':')
        if h == '00':
            h = 0
        else:
            h = int(h.lstrip('0'))
        if m == '00':
            m = 0
        else:
            m = int(m.lstrip('0'))
        return h * 60 + m
    basic_time, basic_charge, unit_time, unit_charge = fee
    car_record = dict()
    for record in records:
        time, car, temp = record.split()
        if car in list(car_record.keys()):
            total_time, in_time = car_record[car]
            if temp == 'OUT':
                park_time = h_to_m(time) - in_time
                car_record[car] = [total_time + park_time, 0]
            else:
                car_record[car] = [total_time, h_to_m(time)]
        else:
            car_record[car] = [0, h_to_m(time)]

    answer = []
    car_num = sorted(list(car_record.keys()))
    for num in car_num:
        total_time, in_time = car_record[num]
        charge = basic_charge
        if in_time or not total_time:
            park_time = h_to_m('23:59') - in_time
            total_time += park_time
        if total_time > basic_time:
            total_time -= basic_time
            if total_time % unit_time:
                charge += ((total_time // unit_time) + 1) * unit_charge
            else:
                charge += (total_time // unit_time) * unit_charge
        answer.append(charge)
    return answer

print(solution(fee, records))