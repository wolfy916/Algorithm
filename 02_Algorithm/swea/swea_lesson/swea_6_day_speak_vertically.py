# 의석이의 세로로 말해요

T = int(input())
for tc in range(1, T+1):
    area = [list(input()) for _ in range(5)]

    max_len = 0
    for x in area:
        if max_len < len(x):
            max_len = len(x)

    speak_list = []
    for j in range(max_len):
        for i in range(5):
            try:
                speak_list += [area[i][j]]
            except:
                continue
    result = ''.join(list(map(str, speak_list)))

    print(f'#{tc} {result}')