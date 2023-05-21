# string 실습 쇠 파이프 자르기

T = int(input())
for tc in range(1, T+1):
    line = list(input().split('()'))

    test_list = []
    sumV = 0
    for i in range(len(line)):
        if line[i] != '':
            for y in line[i]:
                if y == '(':
                    test_list += [1]
                elif y == ')':
                    sumV += test_list[-1]
                    test_list = test_list[:len(test_list)-1]

        if i != 0:
            for j in range(len(test_list)):
                test_list[j] += 1

        if i == 0 and line[i] != '':
            for j in range(len(test_list)):
                test_list[j] += 1

    print(f'#{tc} {sumV}')