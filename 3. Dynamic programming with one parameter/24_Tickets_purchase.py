def count_min_time(a, b, c, n):
    dp = [0] * (n + 3)

    for i in range(3, n + 3):
        dp[i] = min(a[i] + dp[i - 1], b[i - 1] + dp[i - 2], c[i - 2] + dp[i - 3])

    return dp[n + 2]


if __name__ == "__main__":
    n = int(input())

    a = [3601, 3601, 3601] + [0] * (n + 3)
    b = [3601, 3601, 3601] + [0] * (n + 3)
    c = [3601, 3601, 3601] + [0] * (n + 3)

    for i in range(3, n + 3):
        a_i, b_i, c_i = map(int, input().split())

        a[i] = a_i
        b[i] = b_i
        c[i] = c_i

    print(count_min_time(a, b, c, n))
