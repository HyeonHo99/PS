import sys

N = int(sys.stdin.readline())
grid = [[10]*N for _ in range(N)] ## 10 means nothing

## get apples
K = int(sys.stdin.readline())
for _ in range(K):
    R,C = map(int,sys.stdin.readline().rstrip().split())
    grid[R-1][C-1] = 11 ## 11 means apple

## get moves
L = int(sys.stdin.readline())
turn_at = []
turn_to = []
i = 0
for _ in range(L):
    X,C = sys.stdin.readline().rstrip().split()
    X = int(X) + 1
    if C == 'D':
        i += 1
    else:
        i -= 1
    turn_at.append(X)
    turn_to.append(i%4)


##settings
vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]  ## 동,남,서,북
seconds = 0
tail = [0, 0]
head = [0, 0]
cur = 0

while True:
    seconds += 1
    if seconds in turn_at:
        cur = turn_to[0]
        del turn_at[0]
        del turn_to[0]
    grid[head[0]][head[1]] = cur
    head[0] += vectors[cur][0]
    head[1] += vectors[cur][1]
    if head[0] == -1 or head[0] == N or head[1] == -1 or head[1] == N: ## out of grid
        break
    if 0 <= grid[head[0]][head[1]] <= 3: ## hit itself
        break
    if grid[head[0]][head[1]] == 10: ## nothing
        r = tail[0]
        c = tail[1]
        v = grid[r][c]
        tail[0] += vectors[v][0]
        tail[1] += vectors[v][1]
        grid[r][c] = 10

# finished
print(seconds)

