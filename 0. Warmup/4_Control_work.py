def find_closest_place(n, k, row_number, place):
    place_number = row_number * 2 - 2 + place
    # print(f"{place_number = }")
    # print()

    front_place_number = place_number - k
    back_place_number = place_number + k

    # print(f"{front_place_number = }")
    # print(f"{back_place_number = }")
    # print()

    front_row_number = (front_place_number + 1) // 2
    front_place = 2 if front_place_number % 2 == 0 else 1
    # print(f"{front_row_number = }")
    # print(f"{front_place = }")
    # print()

    back_row_number = (back_place_number + 1) // 2
    back_place = 2 if back_place_number % 2 == 0 else 1
    # print(f"{back_row_number = }")
    # print(f"{back_place = }")
    # print()

    if (
        back_row_number - row_number <= row_number - front_row_number
        and back_place_number <= n
    ):
        return (back_row_number, back_place)

    elif front_place_number > 0:
        return (front_row_number, front_place)

    else:
        return (-1,)


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    row_number = int(input())
    place = int(input())

    # 2 2
    # n = 25
    # k = 2
    # row_number = 1
    # place = 2

    # -1
    # n = 25
    # k = 13
    # row_number = 7
    # place = 1

    # 1 1
    # n = 8
    # k = 3
    # row_number = 2
    # place = 2

    print(*find_closest_place(n, k, row_number, place))
