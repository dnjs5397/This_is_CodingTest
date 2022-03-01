N = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()
M = int(input())
order = list(map(int, input().split(' ')))
result = []
for i in order:
    tmp = 'no'
    start = 0
    end = N-1
    while start <= end:
        mid = (start + end) // 2
        if (arr[mid] == i):
            tmp = "yes"
            break
        elif arr[mid] < i:
            start = mid + 1
        else:
            end = mid -1 
    result.append(tmp)
    
for i in result:
    print(i, end=' ')