# 네트워크 연결
# 크루스칼 알고리즘
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 부모 노드를 찾는 함수
def find_par(x, par):
    while x != par[x]:
        x = find_par(par[x], par)
    return x

# [C] 부모 노드 번호를 병합하는 함수
def union(x, y, par):
    X = find_par(x, par)
    Y = find_par(y, par)
    par[max(X, Y)] = min(X, Y)

# [D] 최소 비용 간선을 선택하는 함수
def solution(links, par):
    cost = 0
    for a, b, c in links:
        if find_par(a, par) != find_par(b, par):
            union(a, b, par)
            cost += c
    return cost

# [main]
if __name__ == '__main__':
    # [1] 데이터 입력 및 초기화
    N, M = map(int, input().split())
    par = list(range(N + 1))
    links = [tuple(map(int, input().split())) for _ in range(M)]
    # [2] 간선들을 비용 기준 오름차순 정렬
    links.sort(key=lambda x: x[2])
    # [3] 출력
    print(solution(links, par))