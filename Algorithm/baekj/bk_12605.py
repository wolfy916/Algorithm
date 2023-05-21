T = int(input())
for tc in range(1, T+1):
    sentence = list(input().split())
    sentence = ' '.join(sentence[::-1])

    print(f'Case #{tc}: {sentence}')