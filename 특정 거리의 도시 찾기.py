import sys

N, M, K, X = map(int ,input().split(' '))
visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split(' '))
    graph[a].append(b)

answer = []
tmp = []
tmp.append((X, 0))
while tmp:
    town, count = tmp.pop(0)
    if count == K:
        answer.append(town)
    elif count < K:
        for i in graph[town]:
            if not visited[i]:
                visited[i] = True
                tmp.append((i, count+1))
                
if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)