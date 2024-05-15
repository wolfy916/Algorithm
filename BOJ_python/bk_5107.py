# 마니또
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 그룹 체크 함수
def solution(links):
    answer = 0
    visited = {k: False for k in links.keys()}
    for k in links.keys():
        if visited[k]: continue
        answer += 1
        while visited[k] == 0:
            visited[k] = True
            k = links[k]
    return answer

# [main]
if __name__ == '__main__':
    tc = 1
    while True:
        N = int(input())
        if N == 0: break
        links = dict()
        for _ in range(N):
            a, b = input().split()
            links[a] = b
        print(tc, solution(links))
        tc += 1

