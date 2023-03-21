def count_working_operating_systems(sectors, n):
    working_operating_systems = 0

    for i in range(n):
        current_left, current_right = sectors[i]
        for j in range(i + 1, n):
            new_left, new_right = sectors[j]
            if new_left <= current_right and new_right >= current_left:
                break
        else:
            working_operating_systems += 1

    return working_operating_systems


if __name__ == "__main__":
    m = int(input())
    n = int(input())

    sectors = [0] * n

    for i in range(n):
        a, b = map(int, input().split())
        sectors[i] = (a, b)

    # print(n)
    # print(sectors)

    # 1
    # n = 3
    # sectors = [(1, 3), (4, 7), (3, 4)]

    # 3
    # n = 4
    # sectors = [(1, 3), (4, 5), (7, 8), (4, 6)]

    # 1
    # n = 3
    # sectors = [(4, 5), (1, 5), (1, 2)]

    print(count_working_operating_systems(sectors, n))
