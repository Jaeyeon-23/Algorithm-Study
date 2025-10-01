from collections import deque

def dfs(V):
    global Visited
    Visited[V] = True
    print(V, end =' ')
    for next in range(1, N+1):
        if not Visited[next] and MyMap[V][next]:
            dfs(next)

def bfs(V):
    q = deque([V])
    Visited[V] = True
    while q:
        here = q.popleft()
        Visited[here] = True
        print(here, end = ' ')
        for next in range(1,N+1):
            if not Visited[next] and MyMap[here][next]:
                Visited[next] = True
                q.append(next)


N, M, V = map(int, input().split())
MyMap = [[0]*(N+1) for _ in range(N+1)]
Visited = [False] * (N+1)
q = []
for _ in range(M):
    a, b = map(int, input().split())
    MyMap[a][b] = 1
    MyMap[b][a] = 1

Visited = [False] * (N+1)
dfs(V)
print()
Visited = [False] * (N+1)
bfs(V)