def count_letters_in_substrings(word):
    letters_count = {}

    n = len(word)

    for i in range(n):
        letter = word[i]
        if letter not in letters_count:
            letters_count[letter] = 0
        letters_count[letter] += (i + 1) * (n - i)

    for letter in sorted(letters_count.keys()):
        print(f"{letter}: {letters_count[letter]}")


if __name__ == "__main__":
    word = input()

    # e: 8
    # h: 5
    # l: 17
    # o: 5
    # word = "hello"

    # a: 44
    # b: 24
    # c: 16
    # word = "abacaba"

    count_letters_in_substrings(word)
