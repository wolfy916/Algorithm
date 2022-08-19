bit = [0] * 3

# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             print(bit)


# 위 코드는 크기가 3인 리스트에 원소를 0과 1로 채우는 모든 경우의 수를 출력한다.
# 위 코드를 재귀함수로 구현해보자

def f(i, N):
    if i == N:
        print(bit)
        return
    else:
        bit[i] = 0
        f(i+1, N)
        bit[i] = 1
        f(i+1, N)

f(0, 3)