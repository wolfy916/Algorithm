# 최대 유량

# 연결되지 않은 파이프들을 모두 잘라내는 함수
def isNotLinked(start):
    if start == "Z":
        return False
    else:
        if start in pipes.keys():
            pipe = pipes[start]
            for i in range(len(pipe)):
                end, Q = pipe[i]
                if isNotLinked(end):
                    del pipes[start][i]
                    if not pipes[start]:
                        del pipes[start]
                        return True
                    else:
                        return False
        else:
            return True

N = int(input())
pipes = dict()
for _ in range(N):
    u, v, Q = input().split()
    if u not in pipes.keys():
        pipes[u] = [(v, int(Q))]
    else:
        pipes[u].append((v, int(Q)))

isNotLinked("A")