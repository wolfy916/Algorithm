# 공주의 정원
import sys
input = sys.stdin.readline

# 월,일을 일자로 변환하는 함수
lst_30 = [4, 6, 9, 11]
def change(m, d):
    day = d - 1
    for i in range(1, m):
        if i not in lst_30:
            if i == 2:
                day += 28
                continue
            day += 31
        else:
            day += 30
    return day

N = int(input())

flower = []
s, e = change(3, 1), change(12, 1)  # 테스트 구간
for j in range(N):
    sm, sd, em, ed = map(int, input().split())
    # 3월 이전에 지거나 11월 이후에 피는 꽃들은 모두 걸러짐
    if 11 < sm or em < 3:
        continue
    else:
        s_day = change(sm, sd)
        # 3월 1일보다 일찍 핀다면 3월 1일에 핀 것으로 변경
        if s_day < s:
            s_day = s

        # 12월 1일보다 늦게 진다면 12월 1일에 진 것으로 변경
        e_day = change(em, ed)
        if e < e_day:
            e_day = e

        flower.append([s_day, e_day])

# 늦게 지는 꽃을 앞으로 정렬시킨 후 일찍 피는 꽃이 앞으로 오게 정렬
flower.sort(key=lambda x: x[1], reverse=True)
flower.sort(key=lambda x: x[0])

select = 0  # 선택한 꽃의 개수
start_day = 0  # 마지막으로 선택한 꽃이 피는 날짜
end_day = 0  # 마지막으로 선택한 꽃이 지는 날짜
for k in range(len(flower)):

    # 첫번째 꽃은 무조건 선택
    if k == 0:
        # 첫번째 꽃이 3월1일에 피어있지 않을 경우 강제 종료
        if flower[k][0] != s:
            print(0)
            sys.exit()
        select += 1
        start_day = flower[k][0]
        end_day = flower[k][1]
        continue

    # 마지막으로 선택한 꽃이 지는 날짜보다 일찍(혹은 같은 날짜에) 지는 꽃은 패스
    if flower[k][1] <= end_day:
        continue

    # 마지막으로 선택한 꽃이 지는 날짜보다 늦게 피는 꽃이 발견되면 강제 종료
    if end_day < flower[k][0]:
        print(0)
        sys.exit()
    else:
        # 이번 꽃이 마지막으로 선택한 꽃보다 일찍 피거나 같이 핀다면
        if flower[k][0] <= start_day:
            if end_day < flower[k][1]:  # 더 늦게 지는 꽃일 경우 선택
                end_day = flower[k][1]  # 지는 날짜만 갱신
        else:
            select += 1  # 선택
            start_day = end_day     # 기준 날짜 갱신
            end_day = flower[k][1]  #

# 마지막으로 선택한 꽃이 지는 날짜가 테스트 구간 끝 날짜보다 작을 경우 불가함으로 판단
if end_day < e:
    print(0)
else:
    print(select)