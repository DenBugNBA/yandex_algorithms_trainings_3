def check_is_lower(index, params):
    sticker_numbers, current_lowest_number = params

    return sticker_numbers[index] < current_lowest_number


def binary_search(left, right, check, params):
    while left < right:
        m = (left + right + 1) // 2

        if check(m, params):
            left = m
        else:
            right = m - 1

    return left


def count_interesting_numbers(sticker_numbers, lowest_numbers):
    for current_lowest_number in lowest_numbers:
        index = binary_search(
            0,
            len(sticker_numbers) - 1,
            check_is_lower,
            (sticker_numbers, current_lowest_number),
        )

        if sticker_numbers[index] < current_lowest_number:
            print(index + 1)
        else:
            print(0)


if __name__ == "__main__":
    n = int(input())
    sticker_numbers = sorted(set((map(int, input().split()))))
    k = int(input())
    lowest_numbers = list(map(int, input().split()))

    # 0
    # 1
    # n = 1
    # sticker_numbers = [5]
    # k = 2
    # lowest_numbers = [4, 6]

    # 3
    # 0
    # 2
    # n = 3
    # sticker_numbers = [1, 50, 100]
    # k = 3
    # lowest_numbers = [300, 0, 75]

    count_interesting_numbers(sticker_numbers, lowest_numbers)
