import sys
sys.setrecursionlimit(100000)

def dfs(v, e):
    global s
    visit[v] = True
    s += doornum[v-1]
    if v == e:
        return
    for num in graph[v]:
        if not visit[num]:
            dfs(num, e)
            



N, Q = map(int, input().split(' '))
doornum = list(map(str, input().split(' ')))
graph = [ [] for i in range(N+1) ]
answer = []

for i in range(2, N+1):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i = i.sort()
for i in range(Q):
    start, end = map(int, input().split(' '))
    s = ''
    visit = [False] * (N+1)
    dfs(start, end)
    answer.append(int(s)%1000000007)

for i in answer:
    print(i)