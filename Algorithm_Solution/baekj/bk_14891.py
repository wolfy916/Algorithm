# 톱니바퀴

# [A] 톱니 바퀴 연결여부를 표기하는 함수
def link_check():
    for i in range(3):
        if gear[i][2] != gear[i+1][6]:  # 전극이 다르다면(연결)
            link[i][i+1] = 1
            link[i+1][i] = 1
        else:
            link[i][i+1] = 0
            link[i+1][i] = 0

delta = [-1, 1]
# [B] 톱니 바퀴 회전 dfs 함수
def rotate(n, d):
    if d == 1:
        gear[n] = [gear[n].pop()] + gear[n]  # 시계방향
    else:
        gear[n].append(gear[n].pop(0))  # 반시계방향

    for di in delta:
        ni = n + di
        # 유효한 톱니바퀴의 인덱스 + visited + 링크 여부
        if 0 <= ni < 4 and not visited[ni] and link[n][ni]:
            visited[ni] = 1
            rotate(ni, -1 * d)

gear = [list(map(int, input())) for _ in '_'*4]
K = int(input())

link = [[0]*4 for _ in '_'*4]  # 연결여부를 표기할 adjM
for _ in '_'*K:
    n, d = map(int, input().split())
    link_check()  # 회전시키기 전 항상 link 갱신
    visited = [0] * 4
    visited[n-1] = 1
    rotate(n-1, d)

result = 0
for i in range(4):
    result += gear[i][0] * 2**i
print(result)