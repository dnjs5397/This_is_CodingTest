N, M = map(int ,input().split(' '))
card = []

for i in range(N):
    tmp = list(map(int, input().split(' ')))
    card.append(min(tmp))

print(max(card))

