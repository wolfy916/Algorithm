# 암호
# from collections import deque as dq

# chars = "abcdefghijklmnopqrstuvwxyz"
# pw = "bbbd"
# cnt = -1
# q = dq([''])
# while q:
#     v = q.popleft()
#     cnt += 1
#     cnt %= 900528
#     if v == pw:
#         print(cnt)
#         break
#     for char in chars:
#         q.append(v + char)

arr = "abcdefghijklmnopqrstuvwxyz"
pw = "bbbd"
cnt = 0
temp = 1

for i in range (len(pw) - 1, -1, -1) :
    idx = arr.find(pw[i])
    cnt = (cnt + temp * (idx + 1)) % 900528
    temp = temp * len(arr) % 900528

print(cnt)