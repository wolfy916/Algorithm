# 재형이식 전깃줄 흑흑..
n = int(input())
lines = [list(map(int, input().split())) for _ in '_' * n]

lines.sort(key=lambda x: abs(x[0]-x[1]))  # 전깃줄 길이가 짧은 순으로 정렬

test = [lines[0]]
cnt = 0
for a, b in lines:
    if a == test[0][0]:
        continue
    else:
        for c, d in test:
            if (a > c and b < d) or (a < c and b > d):
                cnt += 1
                break
        else:
            test += [[a, b]]
print(cnt)
