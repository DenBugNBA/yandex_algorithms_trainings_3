def can_rearrange_wagons(wagon_numbers, n):
    current_needed = 1

    stack = []

    for i in range(n):
        if wagon_numbers[i] == current_needed:
            current_needed += 1

        else:
            while stack and wagon_numbers[i] > stack[-1]:
                if stack.pop() == current_needed:
                    current_needed += 1
                else:
                    return "NO"
            stack.append(wagon_numbers[i])

    while stack:
        if stack.pop() == current_needed:
            current_needed += 1
        else:
            return "NO"

    return "YES"


if __name__ == "__main__":
    n = int(input())
    wagon_numbers = list(map(int, input().split()))

    print(can_rearrange_wagons(wagon_numbers, n))
