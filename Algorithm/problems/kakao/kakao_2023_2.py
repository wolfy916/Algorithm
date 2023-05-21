cap = 2
n = 7
deliveries = [0] + [1, 0, 2, 0, 1, 0, 2]
pickups = [0] + [0, 2, 0, 1, 0, 2, 0]
add_d = 0
answer = 0
i = n
while i != 0:
    if pickups[i] >= cap:
        deliveries[i] -= cap
        pickups[i] -= cap
        answer += 2*(i+add_d)

    elif pickups[i] < cap and i >= 1:
        deliveries[i-1] += deliveries[i]
        pickups[i-1] += pickups[i]
        if pickups[i] <= 0 and deliveries[i] <= 0:
            add_d = 0
        else:
            add_d += 1
        i -= 1
else:
    if pickups[i] >= 0 or deliveries[i] >= 0:
        answer += 2*(i+add_d)

print(answer)