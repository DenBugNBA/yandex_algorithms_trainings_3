def count_max_string_beauty(k, s):
    letters = set(s)

    max_beauty = 0

    for letter in letters:
        current_letter_count = 0

        start = 0
        for end in range(len(s)):
            if s[end] == letter:
                current_letter_count += 1

            while not end - start + 1 - current_letter_count <= k:
                if s[start] == letter:
                    current_letter_count -= 1

                start += 1

            max_beauty = max(max_beauty, end - start + 1)

    return max_beauty


if __name__ == "__main__":
    k = int(input())
    s = input()

    # 4
    # k = 2
    # s = "abcaz"

    # 3
    # k = 2
    # s = "helto"

    print(count_max_string_beauty(k, s))
