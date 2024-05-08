# 인간-컴퓨터 상호작용
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 구간합을 구하기 위한 dict 생성
def make_dict(S):
    # dict 생성
    ref = dict()
    for i in range(len(S)):
        s = S[i]
        if not ref.get(s):
            ref[s] = [0] * (len(S) + 1)
        ref[s][i+1] += 1

    # 구간합을 구하기 위한 누적합
    for s in ref.keys():
        for i in range(1, len(S) + 1):
            ref[s][i] += ref[s][i-1]

    return ref

# [main]
if __name__ == '__main__':
    S = input()
    ref = make_dict(S)
    q = int(input())
    for _ in range(q):
        char, l, r = input().split()
        if ref.get(char):
            print(ref[char][int(r) + 1] - ref[char][int(l)])
        else:
            print(0)