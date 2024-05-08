# N = int(input())
# target = input()
# answer = 0

# for _ in range(N-1):
#     compare = target[:]
#     word = input()  # 새로운 단어
#     cnt = 0
#
#     for w in word:
#         if w in compare:
#             compare.remove(w)
#         else:
#             cnt += 1
#
#     if cnt < 2 and len(compare) < 2:
#         answer += 1

N = int(input())
target = input()
answer = 0

target_cnt = [0] * 26
for t in target:
    target_cnt[ord(t) - 65] += 1

for _ in range(N - 1):
    word = input()
    word_cnt = [0] * 26
    for w in word:
        word_cnt[ord(w) - 65] += 1

    cnt = 0
    flag1 = flag2 = flag3 = True
    for i in range(26):
        tmp = target_cnt[i] - word_cnt[i]
        if tmp == 1:
            if flag1:
                flag1 = False
            else:
                flag3 = False
                break
            cnt += tmp

        if tmp == -1:
            if flag2:
                flag2 = False
            else:
                flag3 = False
                break
            cnt += tmp

        if abs(tmp) >= 2:
            flag3 = False
            break

    if flag3 and abs(cnt) < 2:
        answer += 1

print(answer)