N =int(input())
arr = [int(input()) for _ in range(N)]
cnt = 0
k=1
while len(arr) != 1: #1번만 남을떄까지
    if 0<k<len(arr)-1:  #2번~끝번까지 매수차례확인
        k +=1           #다음 매수차례
    else:
        k=1             #끝번이면 다시 1부터
    if arr[k] <arr[0]:  #1번보다 낮으면 pop
        arr.pop(k)
    elif arr[k] >= arr[0]:#같거나 크면 줄이고 본인 up
        arr[0] +=1
        arr[k] += -1
        cnt +=1          #매수한거니 +1
print(cnt)