# 문자열

def solution(s):
    answer = 1001
    for i in range(1, len(s)):
        idx = result = 0
        cnt = 1
        flag = False
        while idx < len(s):
            compare = s[idx: idx + i]
            if compare == s[idx + i: idx + 2 * i]:
                flag = True
                cnt += 1
            else:
                if flag:
                    result += (cnt-1) * i - len(str(cnt))
                    cnt = 1
                    flag = False
            idx += i
        else:
            if flag:
                result += (cnt-1) * i - len(str(cnt))
        answer = min(answer, len(s) - result)
    if answer == 1001:
        answer = len(s)
    return answer

s = "aaaaaaaaaa"
print(solution(s))