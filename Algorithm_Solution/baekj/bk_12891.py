# DNA 비밀번호
import sys

# [A] 입력 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] a부터 b - 1까지의 부분 문자열 상태를 생성하는 함수
def make_dna_state(a, b):
    global current, valid
    current = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    while b <= S:
        for i in range(a, b):
            if current.get(DNA[i]) >= 0:
                current[DNA[i]] += 1
            else:
                current = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
                b += i - a + 1
                a += i - a + 1
                break
        else:
            break

    for dna in condition.keys():
        check[dna] = True if condition[dna] <= current[dna] else False

    return a, b


# [C] 부분 문자열이 유효한 상태인지 판별하는 함수
def is_valid():
    for dna in condition.keys():
        if not check[dna]:
            return False
    return True

# [1] 입력
S, P = map(int, input().split())
DNA = input()
a, c, g, t = map(int, input().split())

# [2] 조건과 상태 dict 선언
condition = {'A': a, 'C': c, 'G': g, 'T': t}
current = dict()
check = {'A': False, 'C': False, 'G': False, 'T': False}
p1, p2 = make_dna_state(0, P)

# [3] 투 포인터를 통한 인덱스 슬라이싱
cnt = 0
while p2 <= S:
    if is_valid():
        cnt += 1
    if p2 < S:
        if current.get(DNA[p2]) >= 0:
            current[DNA[p1]] -= 1
            current[DNA[p2]] += 1
            check[DNA[p1]] = True if condition[DNA[p1]] <= current[DNA[p1]] else False
            check[DNA[p2]] = True if condition[DNA[p2]] <= current[DNA[p2]] else False
            p1 += 1
            p2 += 1
        else:
            if p2 <= S:
                p1, p2 = make_dna_state(p1, p2)
    else:
        break

print(cnt)