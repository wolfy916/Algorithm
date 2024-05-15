'''
1. stack push 구현
def push(S, x):
    top += 1
    if top >= STACK_SIZE
        error overflow; -> 디버깅용
    else
        S[top] = x;

2. stack pop 구현
def pop(S):
    if top < 0
        error underflow
    else
        top -= 1
        return S[top + 1];
'''