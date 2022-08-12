# IM course > string > 3차시 : 문자열 비교

T = int(input())
for tc in range(1, T+1):
    s1 = list(input())
    s2 = list(input())

    result = 0
    for i in range(len(s2)-len(s1)+1):
        cnt = 0
        for j in range(len(s1)):
            if s1[j] == s2[i+j]:
                cnt += 1

        if cnt == len(s1):
            result = 1

    print(f'#{tc} {result}')