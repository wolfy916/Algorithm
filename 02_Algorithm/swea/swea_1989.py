# swea 1989. 초심자의 회문 검사

# 회문이란? 역순으로 배치해도 완벽히 같은 단어 ex) level..
# 멍청하게도 중심 문자를 제외한 모든 알파벳을 비교하는 코드를 짰지만
# 정현이는 reverse(), reversed() 를 사용하여 간단하게 이 문제를 풀어냈다.
# reverse()는 return값이 없고, reversed()는 역순의 주소를 return 하기 때문에 list로 감싸서 사용해야한다.

test_case_n = int(input())
 
i = 0
while i < test_case_n:
 
    test_word = input()
    test_word_list = []
 
    for k in test_word:
        test_word_list.append(k)
 
    list_length = int(len(test_word_list))
    m = 0
 
    while m < ((list_length-1)/2):
 
        result=[]
 
        if test_word_list[m] != test_word_list[list_length-(m+1)]:
            result.append(0)
        else:
            result.append(1)
        m+=1
 
    result.sort()
 
    if result[0] == 0 :
        print("#{0} 0".format(i+1))
    else:
        print("#{0} 1".format(i+1))
    i+=1