## Get input, initialize matrix, visited
N, M = map(int, input().split())
matrix = []
shortcut = []

for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)
    shortcut.append([-1] * M)

## 방향벡터 right,down,left,up
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


## dfs
def dfs(y, x):
    global N, M
    global shortcut

    if y == N - 1 and x == M - 1:
        return 1

    if shortcut[y][x] != -1:
        return shortcut[y][x]

    else:
        shortcut[y][x] = 0
        for i in range(4):
            next_y = y + dy[i]
            next_x = x + dx[i]

            if 0 <= next_y < N and 0 <= next_x < M and matrix[next_y][next_x] < matrix[y][x]:
                shortcut[y][x] += dfs(next_y, next_x)

        return shortcut[y][x]


answer = dfs(0, 0)
print(answer)

for el in shortcut:
    print(el)
