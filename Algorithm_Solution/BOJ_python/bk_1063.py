king, rock, nums = input().split()

rock = [8-int(rock[1]), ord(rock[0])-65]
king = [8-int(king[1]), ord(king[0])-65]

move ={'R':[0, 1], 'L':[0, -1], 'B':[1, 0], 'T':[-1, 0], 'RT':[-1, 1], 'RB':[1, 1], 'LT':[-1, -1], 'LB':[1, -1]}

for num in range(int(nums)):
    cmd = input()
    king = [x + y for x,y in zip(king, move[cmd])]
    if rock == king:
        rock = [x + y for x,y in zip(rock, move[cmd])]
        if not (-1 < rock[0] < 8) or not(-1 < rock[1] < 8):
            rock = [x - y for x,y in zip(rock, move[cmd])]
            king = [x - y for x,y in zip(king, move[cmd])]
    if not (-1 < king[0] < 8) or not(-1 < king[1] < 8):
        king = [x - y for x,y in zip(king, move[cmd])]

print(chr(king[1]+65)+str(8-king[0]))
print(chr(rock[1]+65)+str(8-rock[0]))
