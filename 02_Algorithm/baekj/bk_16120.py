# PPAP
import sys
string = list(sys.stdin.readline().rstrip('\n'))

PPA = ['P', 'P', 'A']
temp_idx = -1
while True:
    temp = []
    for char in string:
        if temp_idx > 1:
            if temp[temp_idx - 2:] == PPA and char == 'P':
                temp.pop()
                temp.pop()
                temp_idx -= 2
                continue
        temp.append(char)
        temp_idx += 1

    if string != temp:
        string = temp
    else:
        break

print("PPAP") if string == ['P'] else print("NP")