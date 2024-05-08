N, K = map(int, input().split())
numbers = list(input())
new_numbers = []
for number in numbers:
    while K and new_numbers:
        if new_numbers[-1] < number:
            new_numbers.pop()
            K -= 1
        else:
            break
    new_numbers.append(number)

if K:
    for _ in range(K):
        new_numbers.pop()

print(''.join(new_numbers))