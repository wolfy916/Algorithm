# 백준 10951 문제는 입력 케이스가 몇개인지 주어지지 않는다.
# 따라서, 반복문의 종료시점에 대한 조건여부로 pass가 갈린다.
# 첫번째 방법은 sys.stdin.readlines()로 입력 파일의 모든 내용을 긁어와서 긁어온 만큼 반복문을 돌리는 것이다.
# 두번째 방법으로는 try except 구문의 사용인데, except에 EOFError(End Of File Error)를 추가하여 해결할 수 있다.

import sys

inputV = sys.stdin.readlines()
for line in inputV:
    A, B = map(int, line.split())
    print(A+B)