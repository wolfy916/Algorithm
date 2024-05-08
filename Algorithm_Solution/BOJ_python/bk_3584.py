# 가장 가까운 공통 조상
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [main]
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        par = [0] * (N + 1)
        for _ in range(N-1):
            A, B = map(int, input().split())
            par[B] = A  # 간선 기록
        A, B = map(int, input().split())

        # A의 조상 노드 기록
        A_path = [A]
        while par[A] != 0:
            A_path.append(par[A])
            A = par[A]

        # B의 조상 노드가 A의 조상 노드와 처음으로 같아질때까지 반복
        while B not in A_path:
            B = par[B]

        print(B)