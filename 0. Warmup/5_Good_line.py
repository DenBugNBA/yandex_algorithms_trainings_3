def count_max_good_string(letters_amount, n):
    good_string = 0

    for i in range(1, n):
        good_string += min(letters_amount[i - 1], letters_amount[i])

    return good_string


if __name__ == "__main__":
    n = int(input())
    letters_amount = [0] * n
    for i in range(n):
        letters_amount[i] = int(input())

    # 2
    # n = 3
    # letters_amount = [1, 1, 1]

    # 3
    # n = 2
    # letters_amount = [3, 4]

    print(count_max_good_string(letters_amount, n))
