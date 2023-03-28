from collections import deque

if __name__ == "__main__":
    queue = deque()

    while True:
        command_data = input().split()

        if len(command_data) == 1:
            if command_data[0] == "pop":
                if len(queue) == 0:
                    print("error")
                else:
                    popped_element = queue.popleft()
                    print(popped_element)

            elif command_data[0] == "front":
                if len(queue) == 0:
                    print("error")
                else:
                    print(queue[0])

            elif command_data[0] == "size":
                print(len(queue))

            elif command_data[0] == "clear":
                queue.clear()
                print("ok")

            if command_data[0] == "exit":
                print("bye")
                break

        else:
            command, element = command_data
            queue.append(int(element))
            print("ok")
