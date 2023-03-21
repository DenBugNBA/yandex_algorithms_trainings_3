def count_prefix_sum_matrix(matrix, n, m):
    prefix_sum_matrix = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix_sum_matrix[i][j] = (
                prefix_sum_matrix[i][j - 1]
                + prefix_sum_matrix[i - 1][j]
                - prefix_sum_matrix[i - 1][j - 1]
                + matrix[i - 1][j - 1]
            )

    return prefix_sum_matrix


def count_sum_in_rectangle(prefix_sum_matrix, start_coordinates, end_coordinates):
    x1, y1 = start_coordinates
    x2, y2 = end_coordinates

    sum_in_rectange = prefix_sum_matrix[x2][y2]

    sum_in_rectange -= prefix_sum_matrix[x1 - 1][y2] - prefix_sum_matrix[0][0]
    sum_in_rectange -= prefix_sum_matrix[x2][y1 - 1] - prefix_sum_matrix[0][0]

    sum_in_rectange += prefix_sum_matrix[x1 - 1][y1 - 1] - prefix_sum_matrix[0][0]

    return sum_in_rectange


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    matrix = [0] * n
    for i in range(n):
        line = list(map(int, input().split()))
        matrix[i] = line

    # n, m, k = 3, 3, 2
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    prefix_sum_matrix = count_prefix_sum_matrix(matrix, n, m)

    # print(prefix_sum_matrix)

    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        print(count_sum_in_rectangle(prefix_sum_matrix, (x1, y1), (x2, y2)))
