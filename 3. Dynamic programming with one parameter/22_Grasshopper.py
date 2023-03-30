def count_number_of_ways(n, k):
    dp = [0] * (k + 30 + 1)

    dp[k + 1] = 1

    for i in range(k + 2, k + n + 1):
        dp[i] = sum(dp[i - k : i])

    # print(dp)

    return dp[k + n]


if __name__ == "__main__":
    n, k = map(int, input().split())
    print(count_number_of_ways(n, k))
