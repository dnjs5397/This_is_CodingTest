move = input()
real_move = []
real_move.append(ord(move[0])-96)
real_move.append(int(move[1]))
count = 0
steps = [(-2, 1), (-2, -1), (2, 1), (2,-1), (1, 2), (1, -2), (-1, 2), (-1, 2)]

for step in steps:
    x = real_move[0] + step[0]
    y = real_move[1] + step[1]
    if (x <= 0 or x >= 9 or y <= 0 or y >= 9):
        pass
    else:
        count += 1

print(count)