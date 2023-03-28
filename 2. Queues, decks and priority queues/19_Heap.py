def push_heap(heap, x):
    heap.append(x)
    pos = len(heap) - 1

    while pos > 0 and heap[pos] > heap[(pos - 1) // 2]:
        heap[pos], heap[(pos - 1) // 2] = heap[(pos - 1) // 2], heap[pos]
        pos = (pos - 1) // 2


def pop_heap(heap):
    max_element = heap[0]

    heap[0] = heap[len(heap) - 1]

    pos = 0

    while (pos * 2) + 2 < len(heap):
        max_descendant_pos = (pos * 2) + 1
        if heap[(pos * 2) + 2] > heap[max_descendant_pos]:
            max_descendant_pos = (pos * 2) + 2

        if heap[pos] < heap[max_descendant_pos]:
            heap[pos], heap[max_descendant_pos] = heap[max_descendant_pos], heap[pos]
            pos = max_descendant_pos
        else:
            break

    heap.pop()

    return max_element


if __name__ == "__main__":
    heap = []

    n = int(input())

    for i in range(n):
        command_line = input().split()

        if len(command_line) == 1:
            print(pop_heap(heap))

        elif len(command_line) == 2:
            push_heap(heap, int(command_line[1]))

        # print(heap, "- heap")
        # print()
