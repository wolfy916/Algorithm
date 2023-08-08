import time

def check(n):
    cnt = 0
    for m in range(2, int(n ** 0.5) + 1):
        if n % m == 0:
            if cnt > 0: return False
            cnt += 1
    return True if cnt == 1 else False

start = time.time()
N, M = 10, 10000
answer = 0
for num in range(N, M):
    if check(num):
        answer += 1
print(answer)
print(time.time() - start)
