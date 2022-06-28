import sys

N,M = map(int,sys.stdin.readline().rstrip().split())
cur_R,cur_C,d = map(int,sys.stdin.readline().rstrip().split())
cur_R,cur_C = cur_R-1,cur_C-1
grid = []
## 1 means wall / 0 means dirt / -1 means clean
for _ in range(N):
    row = list(map(int,sys.stdin.readline().rstrip().split()))
    grid.append(row)

cleaned = 0
while True:
    if grid[cur_R][cur_C] == 0:
        grid[cur_R][cur_C] = -1
        cleaned += 1



# print(N,M)
# print(cur_R,cur_C,d)
# for e in grid:
#     print(e)

