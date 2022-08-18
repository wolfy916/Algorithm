C = int(input())
for tc in range(1, C+1):
    InputV = list(map(int, input().split()))

    student_cnt = 0
    avg_score = sum(InputV[1:]) / InputV[0]
    for x in InputV[1:]:
        if x > avg_score:
            student_cnt += 1
    print(f'{student_cnt * 100 / InputV[0] : .3f}%')
