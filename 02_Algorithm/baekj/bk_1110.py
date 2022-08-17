N = int(input())
test_num = N
i = 0
while True:
    if test_num < 10:
        test_num = 11 * test_num
    else:
        test_num = (test_num%10)*10 + (test_num//10 + test_num%10)%10
    i += 1
    if test_num == N:
        print(i)
        break