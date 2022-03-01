N = int(input())
N = str(N)
answer = []
for i in range(len(N)):
    answer.append(int(N[i]))

if (sum(answer[len(N)//2:]) == sum(answer[:len(N)//2])):
    print("LUCKY")
else:
    print("READY")