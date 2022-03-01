N, M = map(int, input().split(' '))
x, y, direction = map(int, input().split(' '))
map_visit = [[0 for col in range(M)] for row in range(N)]
map_visit[x][y] = 1
map_state = []
count = 0
for i in range(N):
    map_state.append(list(map(int, input().split(' '))))
    

while(1):
    direction -= 1
    if (direction == -1):
        direction = 3
    
    if direction == 0:
      a =1
    if direction == 1:
        a =1
    if direction == 2:
        a =1
    if direction == 3:  a =1