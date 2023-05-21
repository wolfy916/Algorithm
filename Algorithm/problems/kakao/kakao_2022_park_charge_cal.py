# 주차 요금 계산

# fee = [180, 5000, 10, 600]
# records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

fee = [1, 461, 1, 10]
records = ["00:00 1234 IN"]

def solution(fee, records):

    # HH:NN(string) -> minute(int) 변환 함수
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
        time, car, state = record.split()
        # dict에 존재하는 차량번호라면
        if car in list(car_record.keys()):
            # value 확인
            total_time, in_time = car_record[car]
            if state == 'OUT':
                # In -> Out 주차한 시간을 총 주차시간에 더해서 기록
                park_time = h_to_m(time) - in_time
                car_record[car] = [total_time + park_time, 0]
            else:
                # In 총 주차시간을 유지하고, 입차한 시각 기록
                car_record[car] = [total_time, h_to_m(time)]
        # dict에 없는 차량번호라면 [총 주차시간, 입차한 시각(분)]으로 기록
        else:
            car_record[car] = [0, h_to_m(time)]

    answer = []
    car_num = sorted(list(car_record.keys()))  # 차량 번호 오름차순으로 정렬
    for num in car_num:
        total_time, in_time = car_record[num]
        charge = basic_charge
        # 입차기록이 남아있거나 총 주차시간이 0이라면 출차시간을 23:59로 계산
        if in_time or not total_time:
            park_time = h_to_m('23:59') - in_time
            total_time += park_time
        # 기본 주차시간 초과 -> 명세에 맞게 계산
        if total_time > basic_time:
            total_time -= basic_time
            if total_time % unit_time:
                charge += ((total_time // unit_time) + 1) * unit_charge
            else:
                charge += (total_time // unit_time) * unit_charge
        answer.append(charge)
    return answer

print(solution(fee, records))