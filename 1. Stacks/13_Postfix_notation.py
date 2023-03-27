def count_expression(postfix_notation):
    stack = []

    for i in range(len(postfix_notation)):
        if postfix_notation[i].isdigit():
            stack.append(int(postfix_notation[i]))

        else:
            second_operand = stack.pop()
            fist_operand = stack.pop()

            if postfix_notation[i] == "+":
                stack.append(fist_operand + second_operand)
            elif postfix_notation[i] == "-":
                stack.append(fist_operand - second_operand)
            elif postfix_notation[i] == "*":
                stack.append(fist_operand * second_operand)

    return stack[0]


if __name__ == "__main__":
    postfix_notation = input().split()
    print(count_expression(postfix_notation))
