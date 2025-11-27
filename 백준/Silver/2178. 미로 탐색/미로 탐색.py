n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def issafe(x, y):
    if 0 <= x < n and 0 <= y < m and maze[x][y] == 1:
        return True
    return False

def bfs():
    queue = []
    queue.append((0, 0, 1))  
    visited[0][0] = True

    while queue:
        x, y, dist = queue.pop(0)  

        if x == n - 1 and y == m - 1:
            return dist

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if issafe(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

print(bfs())