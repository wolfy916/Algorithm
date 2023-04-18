# k진수에서 소수 개수 구하기

n = 437674
k = 3

# n = 110011
# k = 10

# n = 17777
# k = 10

def solution(n, k):
    answer = 0
    # 10진수면 바로 string으로 변환
    if k == 10:
        k_num = str(n)

    # 10진수가 아니라면
    else:
        k_num = ''
        while n > 0:
            temp = 1
            cnt = 0
            # k의 cnt 제곱이 n을 처음 초과할 때를 찾음
            while temp <= n:
                temp *= k
                cnt += 1
            # 초과하기 직전으로 돌림
            temp //= k
            cnt -= 1
            # k진수의 cnt번째 자리에 가능한 최대값을 찾음
            for i in range(k+1):
                if temp * i > n:
                    temp *= i-1
                    break

            # n에 뺄셈을 하며, 다음 자리 숫자도 탐색함
            n -= temp

            # str값이 비어있지 않다면
            if k_num:
                # 이전 자리와 현재 계산한 자리의 자릿수 차이만큼 0을 추가
                for _ in range(prev-cnt-1):
                    k_num += '0'
                prev = cnt
            # str값이 비어있다면(k진수의 맨 앞자리를 기록할 때)
            else:
                prev = cnt
            # k진수에 추가
            k_num += str(i-1)

    # 0을 경계로 숫자들을 뽑아냄
    number_lst = list(k_num)
    stack = []
    num_lst = []
    for num in number_lst:
        # 0이 아닐때 숫자를 stack에 append
        if num != '0':
            stack.append(num)
        else:
            # string 숫자들을 합쳐서 하나의 숫자로 바꿈
            if len(stack):
                num_lst.append(int(''.join(stack[:])))
                stack.clear()
    # k진수를 다 돌았을때 한번 더 작업 반복 (마지막에 0이 아닐수 있음)
    else:
        if len(stack):
            num_lst.append(int(''.join(stack[:])))

    # 뽑아낸 숫자들 중 소수를 탐색
    for num in num_lst:
        if num == 1:
            continue
        divide = 2
        limit = num
        while divide < limit:
            # 1과 자기자신 사이의 숫자들로 나머지 연산 진행
            # 나머지가 없을 경우 합성수임
            if num % divide:
                limit = num // divide
                divide += 1
            else:
                break
        # while문이 break로 종료되지 않았다면 = 소수 확정
        else:
            answer += 1

    return answer

print(solution(n, k))