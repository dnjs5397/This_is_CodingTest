N, M = map(int, input().split(' '))
rice = list(map(int, input().split(' ')))
H = max(rice)
for i in range(H, 0, -1):
    result = 0
    for j in rice:
        if j - i > 0:
            result += j - i
    if result == M:
        print(i)
        exit(0)
        
    