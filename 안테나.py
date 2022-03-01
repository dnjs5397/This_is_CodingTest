# 백준 18310
N = int(input())
distance = list(map(int, input().split(' ')))
distance.sort()
print(distance[(N-1)//2])