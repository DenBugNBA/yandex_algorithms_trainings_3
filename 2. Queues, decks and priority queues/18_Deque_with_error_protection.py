from collections import deque

if __name__ == "__main__":
    current_deque = deque()

    while True:
        command_data = input().split()

        if len(command_data) == 1:
            if command_data[0] == "size":
                print(len(current_deque))

            elif command_data[0] == "clear":
                current_deque.clear()
                print("ok")

            elif command_data[0] == "exit":
                print("bye")
                break

            else:
                if len(current_deque) == 0:
                    print("error")

                elif command_data[0] == "pop_front":
                    popped_element = current_deque.popleft()
                    print(popped_element)

                elif command_data[0] == "pop_back":
                    popped_element = current_deque.pop()
                    print(popped_element)

                elif command_data[0] == "front":
                    print(current_deque[0])

                elif command_data[0] == "back":
                    print(current_deque[-1])

        elif len(command_data) == 2:
            command, element = command_data

            if command == "push_front":
                current_deque.appendleft(int(element))

            elif command == "push_back":
                current_deque.append(int(element))

            print("ok")
