def find_migration_cities(average_prices, n):
    stack = []

    result_cities = [0] * n

    for i in range(n):
        current_average_price = average_prices[i]

        while stack and current_average_price < stack[-1][0]:
            result_cities[stack.pop()[1]] = i

        stack.append((current_average_price, i))

    while stack:
        result_cities[stack.pop()[1]] = -1

    return result_cities


if __name__ == "__main__":
    n = int(input())
    average_prices = list(map(int, input().split()))
    print(*find_migration_cities(average_prices, n))
