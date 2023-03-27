if __name__ == "__main__":
    stack = []

    while True:
        command_data = input().split()

        if len(command_data) == 1:
            if command_data[0] == "pop":
                if stack == []:
                    print("error")
                else:
                    popped_element = stack.pop()
                    print(popped_element)

            elif command_data[0] == "back":
                if stack == []:
                    print("error")
                else:
                    print(stack[-1])

            elif command_data[0] == "size":
                print(len(stack))

            elif command_data[0] == "clear":
                stack = []
                print("ok")

            if command_data[0] == "exit":
                print("bye")
                break

        else:
            command, element = command_data
            stack.append(int(element))
            print("ok")
