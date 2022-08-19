# 배열 안에 t가 있으면 1, 아니면 0을 출력
def f(i, N, t):
    if i == N:
        return 0  # 배열에 t가 없는 경우, 0을 return
    elif A[i] == t:
        return 1  # 배열에 t가 있는 경우, 0을 return
    else:
        return f(i+1, N, t)  # 다음 탐색을 진행하며, return 되어진 값을 그대로 계속 가져옴


A = [1, 2, 3]
t = 0
print(f(0, 3, t))