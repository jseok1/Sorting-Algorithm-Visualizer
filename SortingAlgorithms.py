# === Sorting Algorithms Implemented in Python ===
def bubble_sort(lst):
    """Bubble sort implementation in Python."""
    k = len(lst) - 1
    while k != 0:
        for i in range(k):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
            yield (lst.copy(), {i, i + 1, k})  # visualization
        k -= 1


def selection_sort(lst):
    """Selection sort implementation in Python."""
    for i in range(len(lst)):
        smallest = i
        for j in range(i, len(lst)):
            if lst[j] < lst[smallest]:
                smallest = j
            yield (lst.copy(), {i, j, smallest})  # visualization
        lst[smallest], lst[i] = lst[i], lst[smallest]
        yield (lst.copy(), {i, smallest})  # visualization


def insertion_sort(lst):
    """Insertion sort implementation in Python."""
    for i in range(1, len(lst)):
        key = lst[i]
        j = i
        while j > 0 and lst[j - 1] > key:
            lst[j] = lst[j - 1]
            yield (lst.copy(), {i, j})  # visualization
            j -= 1
        lst[j] = key
        yield (lst.copy(), {i, j})  # visualization


def merge_sort(lst):
    """Merge sort implementation in Python."""
    yield from _merge_sort(lst, 0, len(lst))


def _merge_sort(lst, start, end):
    """Mutating merge sort implementation in Python."""
    if end - start < 2:
        pass
    else:
        mid = start + len(lst[start:end]) // 2
        yield from _merge_sort(lst, start, mid)
        yield from _merge_sort(lst, mid, end)
        yield from _merge(lst, start, mid, end)


def _merge(lst, start, mid, end):
    """Helper function for merge sort."""
    left = start
    right = mid
    merged = []
    while left < mid and right < end:
        if lst[left] < lst[right]:
            merged.append(lst[left])
            left += 1
        else:
            merged.append(lst[right])
            right += 1

    while left < mid:
        merged.append(lst[left])
        left += 1
    while right < end:
        merged.append(lst[right])
        right += 1

    for i in range(len(merged)):
        lst[start + i] = merged[i]
        yield (lst.copy(), {start + i, start, end})


# def quick_sort(lst):
#     """Quick sort implementation in Python."""
#     yield from _quick_sort(lst, 0, len(lst))
#
#
# def _quick_sort(lst, start, end):
#     """Mutating quick sort implementation in Python using the Hoare partition
#     scheme."""
#     if end - start < 2:
#         pass
#     else:
#         wrapper = set()
#         yield from _partition(lst, start, end, wrapper)
#         pivot = wrapper.pop()
#         yield (lst.copy(), {pivot})
#         yield from _quick_sort(lst, start, pivot)
#         yield from _quick_sort(lst, pivot + 1, end)
#
#
# def _partition(lst, start, end, wrapper):
#     """Helper function for quick sort."""
#     pivot = lst[start]
#     i = start + 1
#     j = end
#     while i < j:
#         if lst[i] < pivot:
#             i += 1
#         else:
#             lst[i], lst[j - 1] = lst[j - 1], lst[i]
#             j -= 1
#         yield (lst.copy(), {i, j, pivot})
#     lst[start], lst[i - 1] = lst[i - 1], lst[start]
#     yield (lst.copy(), {i, j, pivot})
#     wrapper.add(i - 1)

def quicksort(lst):
    if len(lst) < 2:   # sorted
        return lst[:]
    else:   # unsorted
        pivot = lst[0]
        smaller, bigger = _partition(lst[1:], pivot)
        partitioned = smaller + [pivot] + bigger
        for i in range(len(lst)):
            lst[i] = partitioned[i]
            yield (lst.copy(), {})
        smaller_sorted = quicksort(smaller)
        bigger_sorted = quicksort(bigger)
        return smaller_sorted + [pivot] + bigger_sorted


def _partition(lst, pivot):
    smaller = []
    bigger = []
    for item in lst:
        if item <= pivot:
            smaller.append(item)
        else:
            bigger.append(item)
    return smaller, bigger




def heap_sort(lst):
    """Heap sort implementation in Python."""
    n = len(lst)

    # Build max heap
    for i in range(n, -1, -1):
        yield from _heapify(lst, n, i)

    for i in range(n - 1, 0, -1):
        # swap
        lst[i], lst[0] = lst[0], lst[i]
        yield (lst.copy(), {0, i})
        # heapify root element
        yield from _heapify(lst, i, 0)


def _heapify(lst, n, i):
    """Helper for heap sort."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and lst[largest] < lst[left]:
        largest = left

    if right < n and lst[largest] < lst[right]:
        largest = right

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        yield (lst.copy(), {i, largest, n})
        yield from _heapify(lst, n, largest)

