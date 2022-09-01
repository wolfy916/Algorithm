from random import *
import requests
import json
from pprint import *

lotto_num_data = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1030')
lotto_num = lotto_num_data.json()

lotto_num_list = []
for i in range(1,7):
    lotto_num_list += [lotto_num[f'drwtNo{i}']]
lotto_num_list += [lotto_num['bnusNo']]
print(lotto_num_list)

score = [0] * 6  # 등수
for i in range(10):  # 1000
    rand_num = []  # 랜덤 리스트
    while len(rand_num) != 7:
        rand_n = randint(1,45)  # 랜덤숫자
        if rand_n not in rand_num:
            rand_num += [rand_n]
    print(rand_num)
    cnt = 0
    for k in range(7):
        if rand_num[k] == lotto_num_list[k]:
            cnt += 1
    
    for l in range(6):
        if l == cnt:
            score[l] += 1

