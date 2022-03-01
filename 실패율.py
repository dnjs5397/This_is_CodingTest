N = 5
stages = [4,4,4,4,4]
for i in range(len(stages)):
    stages[i] -= 1
result = []
challenge = [0] * N
fail = [0] * N
for i in stages:
    if (i == N):
        for j in range(len(challenge)):
            challenge[j] += 1
    else:
        for j in range(i+1):
            challenge[j] += 1
        fail[i] += 1

for i in range(N):
    if (challenge[i] == 0):
        result.append((i+1, 0))
    else:
        fail[i] = fail[i] / challenge[i]
        result.append((i+1, fail[i]))

result.sort(key = lambda x : x[1], reverse=True)
answer = []
for i in range(N):
    answer.append(result[i][0])
print(answer)