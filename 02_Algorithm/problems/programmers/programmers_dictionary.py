# 모음사전

word = "AAAE"

def solution(word):
    # temp = 방문 문자열, value = 몇번째인지, word = 입력값
    def dfs(temp, value, word):
        # 매칭 성공시 출력할 값과 True 리턴
        if temp == word:
            return (value, True)
        else:
            for i in range(5):
                if len(temp) < 5:  # 문자열 길이 제한
                    value += 1  # 몇번째 탐색인지 카운트
                    v, b = dfs(temp + chars[i], value, word)  # 카운트 값을 리턴해서 들고옴
                    if b:  # 답을 찾았다면
                        return (v, True)  # 계속 리턴
                    else:  # 답을 못찾았다면
                        value = v  # 들고 온 카운트값으로 갱신

        # 답을 못찾았으면 카운트값과 False 리턴
        return (value, False)

    chars = ["A", "E", "I", "O", "U"]
    return dfs('', 0, word)[0]

print(solution(word))