from itertools import permutations
N = int(input())
coin = list(map(int, input().split(' ')))
answer = []
for i in range(N):
    tmp = list(permutations(coin, i+1))
    for j in range(len(tmp)):
        answer.append(sum(tmp[j]))
    
answer = set(answer)
for i in range(1, sum(coin)+2):
    if i not in answer:
        print(i)
        exit(0)
        
        
### 모범답안
# target = 1
# for x in data:
     # 만들 수 없는 금액을 찾으면 반복 종료
#     if target < x:
#         break
#     target += x #target 전까지의 동전은 있으므로 x만큼 더해줘야 한다

# print(target)
