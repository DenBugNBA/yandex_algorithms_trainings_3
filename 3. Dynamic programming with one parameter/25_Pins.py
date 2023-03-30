def count_min_length_of_threads(coordinates, n):
    dp = [0] * n

    dp[0] = coordinates[1] - coordinates[0]
    dp[1] = coordinates[1] - coordinates[0]

    for i in range(2, n):
        dp[i] = min(
            dp[i - 2] + coordinates[i] - coordinates[i - 1],
            dp[i - 1] + coordinates[i] - coordinates[i - 1],
        )

    # print(f"{dp = }")

    return dp[n - 1]


if __name__ == "__main__":
    n = int(input())
    coordinates = sorted(map(int, input().split()))

    # 5
    # n = 6
    # coordinates = [3, 4, 6, 12, 13, 14]

    # 5
    # n = 4
    # coordinates = [1, 2, 3, 7]

    # 4400
    # n = 10
    # coordinates = [682, 2478, 2517, 2816, 4980, 5839, 6414, 7667, 8802, 8995]

    # print(f"{coordinates = }")

    print(count_min_length_of_threads(coordinates, n))
