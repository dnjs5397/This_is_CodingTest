# 백준 10825
students = []
N = int(input())
for i in range(N):
    tmp = input().split()
    temp = (tmp[0], int(tmp[1]), int(tmp[2]), int(tmp[3]))
    students.append(temp)

students.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in students:
    print(i[0])