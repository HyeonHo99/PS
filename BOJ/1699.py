def get_dp(N,dp):
    if N == (int(N ** (1 / 2))) ** 2:
        return 1
    else:
        min_cnt = N
        sqrt = N**(1/2)
        if sqrt > int(sqrt):
            sqrt = int(sqrt) + 1
        else:
            sqrt = int(sqrt)
        for i in range(1, sqrt):
            if min_cnt > (dp[N-i**2] + 1):
                min_cnt = dp[N-i**2] + 1
        return min_cnt

if __name__ == "__main__":
    N = int(input())

    if N == (int(N**(1/2)))**2:
        print(1)
    else:
        dp = [0,1,2,3]

        if N<=3:
            print(dp[N])
        else:
            for n in range(4,N+1):
                dp.append(get_dp(n,dp))
            print(dp[N])