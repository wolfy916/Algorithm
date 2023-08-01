# 추월
import sys

def input():
    return sys.stdin.readline().rstrip('\n')

N = int(input())
car_dict = dict()
for i1 in range(N):
    car_id = input()
    car_dict[car_id] = i1

car_lst = []
for _ in range(N):
    car_id = input()
    car_lst.append(car_id)

cnt = 0
for i2, car_id in enumerate(car_lst):
    for i3 in range(i2 + 1, N):
        if car_dict[car_lst[i3]] < car_dict[car_lst[i2]]:
            cnt += 1
            break

print(cnt)