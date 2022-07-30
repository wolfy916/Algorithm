# swea 1946. 간단한 압축 풀기

def compression ():
    N = int(input())
    for j in range(N): # range(N): 0부터 세어, N개를 생성
        n = int(input())
        print(f'#{j+1}') # print(f'{변수}') : f 를 사용하여 변수를 편하게 출력가능
        C_i=[]
        K_i=[]
        X = ''
        for i in range(n):
            a, b = map(str,input().split())
            C_i.append(str(a)); K_i.append(int(b)) # .append : 문자열 뒤에 문자 추가 !
            for m in range(K_i[i]):
                X = X[:] + C_i[i]
 
        X_i = len(X)//10
        X_r = len(X)%10
 
        if X_r != 0:
            X_i+=1
 
        for o in range(X_i):
            if o == 0:
                print("{0}".format(X[:10]))
            elif o == X_i:
                print("{0}".format(X[(o*10):]))
            else:
                print("{0}".format(X[(o*10):((o*10)+10)]))
     
compression()