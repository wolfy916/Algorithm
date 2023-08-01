# 옥상 정원 꾸미기
import sys

def input():
    return sys.stdin.readline().rstrip('\n')

N = int(input())
buildings = [int(input()) for _ in range(N)]
temp = [buildings[0]]
answer = 0
for i in range(1, N):
    if temp[0] > buildings[i]:
        while temp and temp[-1] <= buildings[i]:
            temp.pop()
            answer += len(temp)
        temp.append(buildings[i])
    else:
        answer += sum(range(len(temp)))
        temp = [buildings[i]]

answer += sum(range(len(temp)))
print(answer)