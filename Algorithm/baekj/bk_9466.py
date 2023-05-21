# 텀 프로젝트
from sys import stdin
input = stdin.readline

for tc in range(1, int(input())+1):
    n = int(input())  # 학생 수
    picks = [0] + list(map(int, input().split()))  # 초이스
    check = [0] * (n+1)
    complete_n = 0  # 팀이 완성된 사람 수 기록
    for i in range(1, n+1):
        if not check[i]:  # 확인 안해본 친구라면
            j = i
            lst = [j]
            check[j] = 1
            while True:
                j = picks[j]  # dfs
                if check[j]:  # 현재 학생이 확인했었던 대상이라면
                    if j in lst:  # 그 친구가 lst에 담겨있는지 확인
                        complete_n += len(lst[lst.index(j):])  # 팀 완성
                    break  # 현재 학생이 lst에 안담겨있다면 lst에 담겨있는 친구들은 모두 팀을 이룰 수 없음
                lst.append(j)
                check[j] = 1

    print(n - complete_n)  # 전체 - 팀을 이룬 학생 수