def is_correct_bracket_sequence(line):
    stack = []

    bracket_pairs = {")": "(", "}": "{", "]": "["}

    for i in range(len(line)):
        if line[i] not in bracket_pairs:
            stack.append(line[i])
        else:
            if stack != [] and bracket_pairs[line[i]] == stack[-1]:
                stack.pop()
            else:
                return "no"

    return "yes" if stack == [] else "no"


if __name__ == "__main__":
    line = input()
    print(is_correct_bracket_sequence(line))
