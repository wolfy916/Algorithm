from django.shortcuts import render
from random import *
import requests
import json

# Create your views here.

def lotto(request):
    lotto_num_data = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1030')
    lotto_num = lotto_num_data.json()

    lotto_num_list = []
    for i in range(1,7):
        lotto_num_list += [lotto_num[f'drwtNo{i}']]
    lotto_num_list += [lotto_num['bnusNo']]

    score = [0] * 6  # 등수
    for i in range(100000):  # 1000
        rand_num = []  # 랜덤 리스트
        while len(rand_num) != 7:
            rand_n = randint(1,45)  # 랜덤숫자
            if rand_n not in rand_num:
                rand_num += [rand_n]
        cnt = 0
        for k in range(7):
            if rand_num[k] == lotto_num_list[k]:
                cnt += 1

        for l in range(6):
            if l == cnt:
                score[l] += 1

    context ={
        'lucky_number': lotto_num_list[:6],
        'bns_number': lotto_num_list[6],
        'no1': score[5],
        'no2': score[4],
        'no3': score[3],
        'no4': score[2],
        'no5': score[1],
        'fail': score[0],
    }

    return render(request, 'pages/lotto.html', context)