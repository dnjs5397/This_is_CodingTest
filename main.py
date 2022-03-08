N = int(input())
people = list(map(int, input().split(' ')))
people.sort()
while(len(people)!=0):
    num = people.pop()
    cnt = 1
    # for i in people:
    #     if i <= num:
            