N = int(input())
meal = list(map(int, input().split(' ')))

val1 = 0
val2 = 0
i1 = 0
i2 = 1
while(i1 < N):
    val1 += meal[i1]
    i1 += 2
while(i2 < N):
    val2 += meal[i2]
    i2 += 2
print(max(val1, val2))