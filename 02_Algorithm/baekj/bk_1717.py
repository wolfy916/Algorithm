# 집합의 표현
import sys
input = sys.stdin.readline

'''
1 <= N <= 1,000,000
1 <= M <= 100,000

연산 입력
0 a b -> a가 포함되어 있는 집합과 b가 포함되어 있는 집합의 합집합
1 a b -> 두 개의 원소가 같은 집합 안에 포함되어 있는지 확인

a, b -> 0이상 N이하의 자연수이며, a = b 일 수도 있다.

출력 조건
연산 1에 대해 YES or NO를 출력
'''

N, M = map(int, input().split())  # N: 0 ~ N 의 집합 N+1개, M: 연산 갯수
num_list = list(range(0, N+1))
groups = []
for _ in '_'*M:
    c, a, b = map(int, input().split())
    if c:
        if num_list[a] == num_list[b]:
            print('YES')
        else:
            print('NO')

    else:
        if num_list[a] == a:
            test_a = [a]
        else:
            test_a = groups.pop(num_list[a])

        if num_list[b] == b:
            test_b = [b]
        else:
            test_b = groups.pop(num_list[a])

        groups.append(test_a+test_b)
        for i in range(len(groups)):
            for num in groups[i]:
                num_list[num] = num