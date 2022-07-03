import sys
sys.setrecursionlimit(10000)

def redistribute(A_map,country_map,N,country_id,sum_list,num_list):
    for r in range(N):
        for c in range(N):
            id = country_map[r][c]
            if num_list[id] >= 2:
                A_map[r][c] = sum_list[id] // num_list[id]


def dfs(A_map,cur_r,cur_c,N,L,R,country_map,country_id,sum_list,num_list):
    country_map[cur_r][cur_c] = country_id
    sum_list[country_id] += A_map[cur_r][cur_c]
    num_list[country_id] += 1
    #top
    if cur_r > 0:
        if country_map[cur_r - 1][cur_c] == -1:
            diff = abs(A_map[cur_r][cur_c] - A_map[cur_r - 1][cur_c])
            if L <= diff and diff <= R:
                dfs(A_map, cur_r - 1, cur_c, N, L, R, country_map, country_id,sum_list,num_list)
    #left
    if cur_c > 0:
        if country_map[cur_r][cur_c-1] == -1:
            diff = abs(A_map[cur_r][cur_c] - A_map[cur_r][cur_c-1])
            if L <= diff and diff <= R:
                dfs(A_map, cur_r, cur_c-1, N, L, R, country_map, country_id,sum_list,num_list)
    #bottom
    if cur_r < N-1:
        if country_map[cur_r + 1][cur_c] == -1:
            diff = abs(A_map[cur_r][cur_c] - A_map[cur_r + 1][cur_c])
            if L <= diff and diff <= R:
                dfs(A_map, cur_r + 1, cur_c, N, L, R, country_map, country_id,sum_list,num_list)
    #right
    if cur_c < N-1:
        if country_map[cur_r][cur_c + 1] == -1:
            diff = abs(A_map[cur_r][cur_c] - A_map[cur_r][cur_c + 1])
            if L <= diff and diff <= R:
                dfs(A_map, cur_r, cur_c + 1, N, L, R, country_map, country_id,sum_list,num_list)


if __name__ == "__main__":
    N, L, R = map(int,sys.stdin.readline().rstrip().split())
    A_map = []
    for _ in range(N):
        A_map.append(list(map(int,sys.stdin.readline().rstrip().split())))

    days = 0
    cond = True
    while cond:
        country_map = [[-1 for _ in range(N)] for _ in range(N)]
        country_id = 0
        sum_list = [0 for _ in range(N * N)]
        num_list = [0 for _ in range(N * N)]
        for r in range(N):
            for c in range(N):
                if country_map[r][c] == -1:
                    dfs(A_map, r, c, N, L, R, country_map, country_id, sum_list, num_list)
                    country_id += 1

        if country_id == N * N:
            cond = False
        else:
            redistribute(A_map, country_map, N, country_id, sum_list, num_list)
            days += 1
    print(days)
