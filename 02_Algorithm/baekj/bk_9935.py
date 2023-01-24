# 문자열 폭발

sentence = input()
bomb = input()
check = 1
while check:
    temp = ''
    check = 0
    if not sentence:
        print('FRULA')
        exit()
    for i in range(len(sentence)):
        for j in range(len(bomb)):
            if sentence[i+j] != bomb[j]:
                temp += sentence[i]
                break
        else:
            check += 1
            flag = True

    sentence = temp
print(sentence)
