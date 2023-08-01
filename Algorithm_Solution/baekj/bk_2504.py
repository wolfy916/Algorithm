# 괄호의 값
def calculate(idx, v, e):
    global is_correct
    value = 0
    tmp = 2 if v == '(' else 3
    if is_correct:
        for i in range(idx + 1, len(string)):
            if not visited[i]:
                visited[i] = 1
                if string[i] in ['( ', '[']:
                    value += calculate(i, string[i], end[string[i]])
                elif string[i] == e:
                    return tmp * value if value else tmp
                else:
                    is_correct = False
                    return 0
    return 0

string = input()
answer = 0
visited = [0] * len(string)
end = {'(': ')', '[': ']'}
is_correct = True
for i in range(len(string)):
    if not is_correct:
        break
    if not visited[i]:
        if string[i] in ['(', '[']:
            visited[i] = 1
            answer += calculate(i, string[i], end[string[i]])
        else:
            is_correct = False

print(answer if is_correct else 0)