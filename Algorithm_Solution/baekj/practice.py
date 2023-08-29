# 문제2
# input()을 3*3으로 변환
# 게임판이 가득찾는지 확인 + 가로3개 세로3개 대각선2개의 라인 확인
# arr[0][0] -> 가로 ,세로
# arr[1][1] -> 가로 ,세로
# arr[2][2] -> 가로 ,세로
# 대각선 2개
# X가 O보다 갯수가 1개 많고 X의 빙고 -> 가능
# O가 X랑 갯수가 같고 O의 빙고 -> 가능
# X가 O보다 1개 많거나 같고 빙고는 없음 -> 가능


# X나 O가 빙고가 있는지 여부를 확인하는 f(str):
def check(word):
    if word == arr[0][0] == arr[1][0] == arr[2][0]:
        return True
    if word == arr[0][0] == arr[0][1] == arr[0][2]:
        return True
    if word == arr[0][0] == arr[1][1] == arr[2][2]:
        return True
    if word == arr[1][1] == arr[1][0] == arr[1][2]:
        return True
    if word == arr[1][1] == arr[0][1] == arr[2][1]:
        return True
    if word == arr[1][1] == arr[2][0] == arr[0][2]:
        return True
    if word == arr[2][2] == arr[2][0] == arr[2][1]:
        return True
    if word == arr[2][2] == arr[0][2] == arr[1][2]:
        return True
    return False
while True:
    str = input()
    if str == 'end':
        break
    else:
        arr = [0] * 3
        dict = {"X":0,"O":0}
        cnt = 0
        for i in range(3):
            arr[i] = list(str[i * 3:i * 3 + 3])
        for i in range(3):
            for j in range(3):
                if arr[i][j] !=".":
                    dict[arr[i][j]] +=1
                else:
                    cnt +=1
        # X가 O보다 갯수가 1개 많고 X의 빙고 Y는 빙고 없음 -> valid
        X,O = "X","O"
        if (dict["X"] == dict["O"] +1) and check(X) and not check(O):
            print("valid")
        # O가 X랑 갯수가 같고 X는 빙고 없고 O의 빙고 -> 가능
        elif (dict["X"] == dict["O"] ) and not check(X) and check(O):
            print("valid")
        # .이 0개 이고 X가 O보다 1개 많고 빙고는 둘다 없음 -> 가능
        elif cnt == 0 and ( dict["X"] == dict["O"] +1)  and not check(X) and not check(O):
            print("valid")
        else:
            print("invalid")