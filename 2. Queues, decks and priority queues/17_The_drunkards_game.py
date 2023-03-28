from collections import deque


def determine_the_winner(first_cards, second_cards):
    for i in range(10**6):
        first_card = first_cards.popleft()
        second_card = second_cards.popleft()

        if first_card == 0 and second_card == 9:
            first_cards.append(0)
            first_cards.append(9)

        elif first_card == 9 and second_card == 0:
            second_cards.append(9)
            second_cards.append(0)

        elif first_card > second_card:
            first_cards.append(first_card)
            first_cards.append(second_card)

        elif second_card > first_card:
            second_cards.append(first_card)
            second_cards.append(second_card)

        if len(first_cards) == 0:
            return ("second", i + 1)
        elif len(second_cards) == 0:
            return ("first", i + 1)

    return ("botva",)


if __name__ == "__main__":
    first_cards = deque(map(int, input().split()))
    second_cards = deque(map(int, input().split()))

    # print(first_cards)
    # print(second_cards)

    print(*determine_the_winner(first_cards, second_cards))
