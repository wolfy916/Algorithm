from multiprocessing import context
from django.shortcuts import render
from random import *
from datetime import datetime
# Create your views here.

def index(request):
    return render(request, 'index.html')

def greeting(request):
    foods = ['apple', 'banana', 'coconut']

    info = {
        'name' : 'woong'
    }

    context = {
        'foods' : foods,
        'info' : info,
    }

    return render(request, 'greeting.html', context)

def dinner(request):
    foods = ['apple', 'banana', 'coconut']

    context = {
        'foods' : foods[randint(0, 2)],
    }

    return render(request, 'dinner.html', context)

def image(request):
    return render(request, 'image.html')

def template_language(request):
    menus = ['족발', '햄버거', '치킨', '초밥', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    empty_list = []
    datetimenow = datetime.now()  # 오늘에 대한 날짜/시각 정보

    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'template_language.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    print(request)
    print(type(request))
    print(request.GET.get('message'))
    message = request.GET.get('message')

    context = {
        'message': message
    }

    return render(request, 'catch.html', context)

def hello(request, name, age):
    context = {
        'name': name,
        'age': age
    }
    return render(request, 'hello.html', context)

def ispal(request, name):

    pal = list(name)
    turn_pal = pal[::-1]
    if pal == turn_pal:
        name = '회문이 맞습니다.'
    else:
        name = '회문이 아닙니다.'
    
    context = {
        'name': name,
    }

    return render(request, 'ispal.html', context)

def lotto(request):
    
    lotto_1030 = [2, 5, 11, 17, 24, 29]
    random_lotto = []
    while len(random_lotto) != 6:
        rand_num = randint(1,46)
        if rand_num not in random_lotto:
            random_lotto += [rand_num]
    matching_num_list = []
    matching_num = 0
    for num in random_lotto:
        if num in lotto_1030:
            matching_num_list += [num]
            matching_num += 1
    random_lotto = ', '.join(list(map(str, random_lotto)))

    context = {
        'lotto_1030': lotto_1030,
        'random_lotto': random_lotto,
        'matching_num_list': matching_num_list,
        'matching_num': matching_num,
    }
    return render(request, 'lotto.html', context)