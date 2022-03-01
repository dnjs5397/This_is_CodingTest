from re import L


N, M, K = map(int, input().split(' '))
number = list(map(int, input().split(' ')))

number.sort()
first = number[N-1]
second = number[N-2]

result = 0

while(1):
    for i in range(K):
        if M == 0:
            break
        result += first
        M -= 1
    if M == 0:
        break
    result += second
    M -= 1
    
print(result)

