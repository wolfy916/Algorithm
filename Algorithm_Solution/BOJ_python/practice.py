from heapq import heappush, heappop

n = int(input())
hq = []
answer = []
for _ in range(n):
    num = int(input())
    if num > 0:
        heappush(hq, num)
    else:
        if len(hq) < 1:
            answer.append(0)
        else:
            answer.append(heappop(hq))

for i in range(len(answer)):
    print(answer[i])