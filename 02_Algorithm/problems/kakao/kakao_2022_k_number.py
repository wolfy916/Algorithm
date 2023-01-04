# k진수에서 소수 개수 구하기

# n = 437674
# k = 3

# n = 110011
# k = 10

n = 17777
k = 10


def solution(n, k):
    answer = 0
    if k == 10:
        test_num = str(n)
    else:
        test_num = ''
        while n > 0:
            temp = 1
            cnt = 0
            while temp <= n:
                temp *= k
                cnt += 1
            temp //= k
            cnt -= 1
            for i in range(k+1):
                if temp * i > n:
                    temp *= i-1
                    break
            n -= temp
            if test_num:
                for _ in range(prev-cnt-1):
                    test_num += '0'
                prev = cnt
            else:
                prev = cnt
            test_num += str(i-1)
    number_lst = list(test_num)
    temp_lst = []
    num_lst = []
    for num in number_lst:
        if not num == '0':
            temp_lst.append(num)
        else:
            if len(temp_lst):
                num_lst.append(int(''.join(temp_lst[:])))
                temp_lst.clear()
    else:
        if len(temp_lst):
            num_lst.append(int(''.join(temp_lst[:])))
    for num in num_lst:
        if num == 1:
            continue
        divide = 2
        limit = num
        while divide < limit:
            if num % divide:
                limit = num // divide
                divide += 1
            else:
                break
        else:
            answer += 1

    return answer

print(solution(n, k))