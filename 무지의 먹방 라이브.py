food_times = [1,1,1,1]
k = 4
index = 0
while(k!=0):
    if (food_times[index]==0):
        if (len(set(food_times)) == 1 and 0 in set(food_times)):
            print(-1)
            exit(0)
        index += 1
        if (index == len(food_times)):
            index = 0
        continue
    food_times[index] -= 1
    index += 1
    k -= 1
    if (index == len(food_times)):
            index = 0
            

while(food_times[index]==0):
    if (food_times[index]==0):
        if (len(set(food_times)) == 1 and 0 in set(food_times)):
            print(-1)
            exit(0)
    index += 1
    if (index == len(food_times)):
        index = 0


print(index+1)

#####################
def solution(food_times, k):
    foods = []
    n = len(food_times) # 음식의 개수
    for i in range(n):
        foods.append((food_times[i], i+1))
        
    foods.sort() # 음식 시간 값으로 정렬
    
    pretime = 0
    for i, food in enumerate(foods): 
        diff = food[0] - pretime
        if diff != 0:
            spend = diff * n
            if spend <= k:
                k -= spend
                pretime = food[0]
            else:
                k %= n
                sublist = sorted(foods[i:], key = lambda x : x[1])
                print(sublist[k][1])
        n -= 1
    print(-1)