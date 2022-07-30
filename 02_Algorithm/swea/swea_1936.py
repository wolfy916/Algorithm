# swea 1936. 1대1 가위바위보 만들기

A, B=map(int, input().split()) # 정수 2개를 동시에 입력 받는다. 예 ) 3 4로 입력 
if A + B == 4:
    if A > B:
        print("B")
    else:
        print("A")
else:
    if A > B :
        print("A")
    else:
        print("B")