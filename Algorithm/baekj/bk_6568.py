# 귀도 반 로썸은 크리스마스날 심심하다고 파이썬을 만들었다

# [A] 십진수 int형 -> 8비트 이진수 string으로 변환
def bi(v):
    if v == 256:
        return '0'*8
    elif v == -1:
        return '1'*8
    result = ''
    for i in range(7, -1, -1):
        if v >= 2**i:
            v -= 2**i
            result += '1'
        else:
            result += '0'
    return result

# [B] 이진수 string -> 십진수 int형으로 변환
def rev_bi(v):
    result = 0
    for i in range(len(v)):
        if v[len(v)-1-i] == '1':
            result += 2**i
    return result

while True:
    try:
        PC = 0  # program counter
        value = '00000000'  # 가산기 값
        data = [input() for _ in '_'*32]  # 주소 0 ~ 31 까지의 메모리 저장소
        while True:
            code = data[PC]
            PC += 1  # PC로 해당 주소의 코드를 불러오고, 코드 실행 전 PC값 증가
            if PC == 32:  # 저장소의 주소가 31까지밖에 없음 (32바이트라서)
                PC = 0
            order_code = code[:3]  # 명령코드
            location_code = code[3:]  # 주소코드(이진수)

            # print('------------------------------')
            # print(f'수행 전 - > PC: {PC-1}, 가산기 값: {value}')
            # print(f'수행해야할 코드: {order_code}')

            if order_code == '000':  # 주소코드가 가르키는 코드를 가산기 값으로 오버라이딩
                data[rev_bi(location_code)] = value
            elif order_code == '001':  # 가산기 값에 주소코드가 가르키는 코드 할당
                value = data[rev_bi(location_code)]
            elif order_code == '010':
                if value == '0'*8:  # 가산기 값이 0일 때, PC에 주소코드 십진수로 변환하여 할당
                    PC = rev_bi(location_code)
            elif order_code == '100':  # 가산기 값 -= 1
                value = bi(rev_bi(value) - 1)
            elif order_code == '101':  # 가산기 값 += 1
                value = bi(rev_bi(value) + 1)
            elif order_code == '110':  # PC에 주소코드 십진수로 변환하여 할당
                PC = rev_bi(location_code)
            elif order_code == '111':  # 종료
                break

            # print(f'수행 결과 -> PC: {PC}, 가산기 값: {value}')
            # print('------------------------------')

        print(value)

    except EOFError:
        break