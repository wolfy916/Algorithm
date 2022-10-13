# (야구공 그림)
from itertools import permutations

N = int(input())
arr = [list(map(int, input().split())) for _ in '_'*N]

player = list(range(1, 9))
lines = list(map(list, permutations(player, 8)))
result = 0
for line in lines:
    play_line = line[0:3] + [0] + line[3:]
    i = 0
    score = 0
    for inning in range(N):
        board_queue = []
        out = 0
        while out != 3:
            playing = play_line[i]
            if arr[inning][playing] == 0:
                out += 1
            elif arr[inning][playing] != 4:
                if board_queue:
                    for j in range(len(board_queue)):
                        board_queue[j] += arr[inning][playing]
                    while board_queue and board_queue[0] >= 4:
                        board_queue.pop(0)
                        score += 1
                board_queue.append(arr[inning][playing])
            else:
                score += len(board_queue) + 1
                board_queue.clear()
            i = (i + 1) % 9

    if result < score:
        result = score

print(result)