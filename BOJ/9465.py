import sys


def get_max_score(n,table):
    if n == 1:
        return max(table[0][0], table[1][0])
    else:
        dp = [[0,0,0] for _ in range(n)]
        dp[0][0] = table[0][0]
        dp[0][1] = table[1][0]

        for i in range(1,n):
            dp[i][0] = max(dp[i-1][1],dp[i-1][2]) + table[0][i]
            dp[i][1] = max(dp[i-1][0],dp[i-1][2]) + table[1][i]
            dp[i][2] = max(dp[i-1][0],dp[i-1][1])
        return max(dp[-1])

if __name__ == "__main__":
    ## input
    T = int(input())
    n_list = []
    table_list = []
    for i in range(T):
        n_list.append(int(input()))
        table = []
        for _ in range(2):
            table.append(list(map(int,sys.stdin.readline().rstrip().split())))
        table_list.append(table)

    for i in range(T):
        print(get_max_score(n_list[i],table_list[i]))