def count_least_operations(n):
    dp = [0, 0] + [i for i in range(1, n)]
    prev_numbers = [0, -1] + [i for i in range(1, n)]

    # print(f"{dp = }")
    # print(f"{prev_numbers = }")
    # print()

    for i in range(1, n):
        # print(f"{i = }")

        product_with_two = i * 2
        if product_with_two <= n and dp[i] + 1 < dp[product_with_two]:
            dp[product_with_two] = dp[i] + 1
            prev_numbers[product_with_two] = i

        product_with_three = i * 3
        if product_with_three <= n and dp[i] + 1 < dp[product_with_three]:
            dp[product_with_three] = dp[i] + 1
            prev_numbers[product_with_three] = i

        increment_with_one = i + 1
        if increment_with_one <= n and dp[i] + 1 < dp[increment_with_one]:
            dp[increment_with_one] = dp[i] + 1
            prev_numbers[increment_with_one] = i

        # print(dp)
        # print(prev_numbers)
        # print()

    # print(f"{dp = }")
    # print(f"{prev_numbers = }")

    answer_operations = [n]

    i = n
    while prev_numbers[i] != -1:
        answer_operations.append(prev_numbers[i])
        i = prev_numbers[i]

    return answer_operations


if __name__ == "__main__":
    n = int(input())

    answer_operations = count_least_operations(n)

    # print(answer_operations)

    print(len(answer_operations) - 1)
    print(" ".join(map(str, answer_operations[::-1])))
