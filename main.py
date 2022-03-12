def nega_clock_even(x,y, direction):
    val = 1
    loop = N-1
    while (1):
        direction %= 4
        if (x==N//2-1 and y==N//2-1) or (x==N//2-1 and y == N//2) or (x==N//2 and y == N//2-1) or (x==N//2 and y == N//2):
            answer[x][y] = val
            break
        for i in range(loop):
            answer[x][y] = val
            if i == loop-1:
                direction = (direction + 1) % 4
            if direction == 0:
                x += 1
            elif direction == 1:
                y += 1
            elif direction == 2:
                x -= 1
            else:
                y -= 1
            val += 1
        loop -= 2

def posi_clock_even(x,y, direction):
    val = 1
    loop = N-1
    while (1):
        direction %= 4
        if (x==N//2-1 and y==N//2-1) or (x==N//2-1 and y == N//2) or (x==N//2 and y == N//2-1) or (x==N//2 and y == N//2):
            answer[x][y] = val
            break
        for i in range(loop):
            answer[x][y] = val
            if i == loop-1:
                direction = (direction + 1) % 4
            if direction == 0:
                y += 1
            elif direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            else:
                x -= 1
            val += 1
        loop -= 2

def nega_clock_odd(x,y, direction):
    val = 1
    loop = N-1
    while (1):
        direction %= 4
        if (x==N//2 and y==N//2):
            answer[x][y] = val
            break
        for i in range(loop):
            answer[x][y] = val
            if i == loop-1:
                direction = (direction + 1) % 4
            if direction == 0:
                x += 1
            elif direction == 1:
                y += 1
            elif direction == 2:
                x -= 1
            else:
                y -= 1
            val += 1
        if loop == 2:
            loop -= 1
        else:
            loop -= 2

def posi_clock_odd(x,y, direction):
    val = 1
    loop = N-1
    while (1):
        direction %= 4
        if (x==N//2 and y==N//2):
            answer[x][y] = val
            break
        for i in range(loop):
            answer[x][y] = val
            if i == loop-1:
                direction = (direction + 1) % 4
            if direction == 0:
                y += 1
            elif direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            else:
                x -= 1
            val += 1
        if loop == 2:
            loop -= 1
        else:
            loop -= 2
            
N = 6
clockwise = True
answer= [[0 for i in range(N)] for j in range(N)]
if N % 2 == 0: # 짝수
    if clockwise == True:
        posi_clock_even(0,0,0)
        posi_clock_even(N-1,0,3)
        posi_clock_even(N-1,N-1,2)
        posi_clock_even(0,N-1,1)
    else:
        nega_clock_even(0,0,0)
        nega_clock_even(N-1,0,1)
        nega_clock_even(N-1,N-1,2)
        nega_clock_even(0,N-1,3)
else:
    if clockwise == True:
        posi_clock_odd(0,0,0)
        posi_clock_odd(N-1,0,3)
        posi_clock_odd(N-1,N-1,2)
        posi_clock_odd(0,N-1,1)
    else:
        nega_clock_odd(0,0,0)
        nega_clock_odd(N-1,0,1)
        nega_clock_odd(N-1,N-1,2)
        nega_clock_odd(0,N-1,3)
for i in answer:
    print(i)