def heapify(arr):
    right_pos_with_descendant = len(arr) // 2 - 1

    for i in range(right_pos_with_descendant, -1, -1):
        pos = i
        # print(pos, "- heapify pos")

        while (pos * 2) + 1 < len(arr):
            max_descendant_pos = (pos * 2) + 1

            if (
                max_descendant_pos + 1 < len(arr)
                and arr[max_descendant_pos + 1] > arr[max_descendant_pos]
            ):
                max_descendant_pos += 1

            if arr[pos] < arr[max_descendant_pos]:
                # print("Swap")
                arr[pos], arr[max_descendant_pos] = arr[max_descendant_pos], arr[pos]
                pos = max_descendant_pos
            else:
                break

        # print(arr)
        # print()


def pop_heap(heap, i):
    max_element = heap[0]

    heap[0] = heap[-1 - i]

    pos = 0

    while (pos * 2) + 2 < len(heap) - i:
        max_descendant_pos = (pos * 2) + 1
        if heap[max_descendant_pos + 1] > heap[max_descendant_pos]:
            max_descendant_pos += 1

        if heap[pos] < heap[max_descendant_pos]:
            heap[pos], heap[max_descendant_pos] = heap[max_descendant_pos], heap[pos]
            pos = max_descendant_pos
        else:
            break

    return max_element


# HeapSort
def pyramid_sorting(arr):
    heapify(arr)
    # print(arr, "- heapified")

    for i in range(0, len(arr)):
        current_max = pop_heap(arr, i)
        arr[-(i + 1)] = current_max

    return arr


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    # 1
    # n = 1
    # arr = [1]

    # 1 3
    # n = 2
    # arr = [3, 1]

    # 2 3 4 5 7 8 10 12 25
    # n = 9
    # arr = [5, 2, 8, 10, 7, 4, 25, 12, 3]

    # 2 3 4 5 7 8 10 11 12 25
    # n = 10
    # arr = [5, 2, 8, 10, 7, 4, 25, 12, 3, 11]

    # print(arr)

    pyramid_sorting(arr)
    print(*arr)
