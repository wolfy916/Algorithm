# 앵무새
N = int(input())
sentence = [list(input().split()) for _ in '_'*N]
L = list(input().split())

result = 1
while L:
    cnt = 0
    word = L[0]
    for i in range(N):
        if sentence[i] and sentence[i][0] == L[0]:
            sentence[i].pop(0)
            L.pop(0)
            cnt += 1
            break

    if cnt == 0:
        result = 0
        break
else:
    for i in range(N):
        if sentence[i]:
            result = 0
            break

if result == 1:
    result = 'Possible'
else:
    result = 'Impossible'

print(result)