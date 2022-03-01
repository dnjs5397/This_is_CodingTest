# 백준 3190
N = int(input())
mapinfo = [[0 for col in range(N+1)] for row in range(N+1)] # 맵의 모든 부분을 0으로 초기화
mapinfo[1][1] = 2 # 뱀이 있는 부분은 2로 표시
snake_direction = 1 # 0 : 위 1 : 오른쪽 2 : 아래 3 : 왼쪽
K = int(input())
for i in range(K):
    tmp1, tmp2 = map(int, input().split(' '))
    mapinfo[tmp1][tmp2] = 1 # 사과가 있는 부분은 1로 표시
L = int(input())
for _ in range(L):
    tmp = input().split(' ')
    second = int(tmp[0])
    direction = tmp[1]