from time import time
from copy import deepcopy

a = [list(range(10000)) for _ in range(10000)]

t1 = time()

b1 = [[] for _ in range(10000)]  # 1번 연산
for i in range(10000):
    b1[i] = a[i][:]

t2 = time()

b2 = [line[:] for line in a]  # 2번 연산

t3 = time()

b3 = deepcopy(a)  # 3번 연산

t4 = time()

print(f'1번 수행시간 : {t2-t1:.10f}초')
print(f'2번 수행시간: {t3-t2:.10f}초')
print(f'3번 수행시간: {t4-t3:.10f}초')
