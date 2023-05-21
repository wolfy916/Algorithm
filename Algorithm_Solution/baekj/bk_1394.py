# 암호
import sys
input = sys.stdin.readline

chars = list(input().rstrip('\n'))
password = input().rstrip('\n')

used_char_idx = [chars.index(p) for p in password]
used_lenV = len(used_char_idx)
chars_lenV = len(chars)

answer = [0] * used_lenV
for i in range(used_lenV):
    if i < used_lenV - 1:
        answer[i] = (answer[i-1] if answer[i-1] else 1) * chars_lenV
    else:
        answer[i] += (answer[i-1] if answer[i-1] else 1) * used_char_idx[i-1] + (answer[i-1] // chars_lenV if answer[i-1] else 1) * (used_char_idx[i] + 1)
print(sum(answer) % 900528)
