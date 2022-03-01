from audioop import reverse


N, K = map(int, input().split(' '))
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))
A.sort()
B.sort(reverse=True)
result = 0
for i in range(K):
    A.pop(0)
    result += B[i]

print(sum(A) + result)

