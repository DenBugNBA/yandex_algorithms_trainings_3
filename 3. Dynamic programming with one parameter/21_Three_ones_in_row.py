def count_sequences(n):
    dp = [0] * 36

    dp[0] = 1
    dp[1] = 2
    dp[2] = 4

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]


if __name__ == "__main__":
    n = int(input())
    print(count_sequences(n))
