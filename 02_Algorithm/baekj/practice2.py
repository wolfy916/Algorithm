N, K = map(int, input().split())
numbers = list(input())
new_numbers = []
while numbers:
    number = numbers.pop(0)
    while K and new_numbers:
        if new_numbers[-1] < number:
            new_numbers.pop()
            K -= 1
        else:
            break
    new_numbers.append(number)
print(''.join(new_numbers))