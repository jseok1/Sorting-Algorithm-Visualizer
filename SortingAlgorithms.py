# === Sorting Algorithms ===
def bubble_sort(lst):
    """Bubble sort implementation in Python."""
    k = len(lst) - 1
    while k > 0:
        for i in range(k):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
            yield (lst.copy(), {i, i + 1, k}, {})
        k -= 1
    yield (lst.copy(), {}, {})


def selection_sort(lst):
    """Selection sort implementation in Python."""
    for i in range(len(lst)):
        smallest = i
        for j in range(i, len(lst)):
            if lst[j] < lst[smallest]:
                smallest = j
            yield (lst.copy(), {i, j, smallest}, {})
        lst[smallest], lst[i] = lst[i], lst[smallest]
        yield (lst.copy(), {i, smallest}, {})
    yield (lst.copy(), {}, {})


def insertion_sort(lst):
    """Insertion sort implementation in Python."""
    for i in range(0, len(lst)):
        key = lst[i]
        j = i
        while j > 0 and lst[j - 1] > key:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            yield (lst.copy(), {i, j - 1, j}, {})
            j -= 1
        lst[j], key = key, lst[j]
        yield (lst.copy(), {i, j}, {})
    yield (lst.copy(), {}, {})


def merge_sort(lst):
    """Used to call merge sort."""
    yield from _merge_sort(lst, 0, len(lst) - 1)
    yield (lst.copy(), {}, {})


def _merge_sort(lst, low, high):
    """Merge sort implementation in Python."""
    if low >= high:
        yield (lst.copy(), {}, {})
    else:
        mid = (low + high) // 2
        yield from _merge_sort(lst, low, mid)
        yield from _merge_sort(lst, mid + 1, high)
        yield from _merge(lst, low, mid, high)


def _merge(lst, low, mid, high):
    """Helper function for merge sort."""
    merged = []
    i = low
    j = mid + 1
    while i < mid + 1 and j < high + 1:
        if lst[i] < lst[j]:
            merged.append(lst[i])
            yield (lst.copy(), {i, j}, {n for n in range(low, high + 1)})
            i += 1
        else:
            merged.append(lst[j])
            yield (lst.copy(), {i, j}, {n for n in range(low, high + 1)})
            j += 1
    while i < mid + 1:
        merged.append(lst[i])
        yield (lst.copy(), {i}, {n for n in range(low, high + 1)})
        i += 1
    while j < high + 1:
        merged.append(lst[j])
        yield (lst.copy(), {j}, {n for n in range(low, high + 1)})
        j += 1
    p = 0
    for q in range(low, high + 1):
        lst[q] = merged[p]
        yield (lst.copy(), {q}, {n for n in range(low, high + 1)})
        p += 1


def quick_sort(lst):
    """Used to call quick sort."""
    yield from _quick_sort(lst, 0, len(lst) - 1)
    yield (lst.copy(), {}, {})


def _quick_sort(lst, low, high):
    """Quick sort implementation in Python."""
    if low >= high:
        yield (lst.copy(), {}, {})
    else:
        pivot = -1
        for p in _partition(lst, low, high):
            pivot = max(p[1]) - 1
            yield p
        yield from _quick_sort(lst, low, pivot)
        yield from _quick_sort(lst, pivot + 1, high)


def _partition(lst, low, high):
    """Helper function for quick sort."""
    pivot = lst[low]
    i = low
    j = high
    while True:
        while lst[i] < pivot:
            yield (lst.copy(), {i, j, low}, {n for n in range(low, high + 1)})
            i += 1
        while lst[j] > pivot:
            yield (lst.copy(), {i, j, low}, {n for n in range(low, high + 1)})
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
            yield (lst.copy(), {i, j, low}, {n for n in range(low, high + 1)})
        else:
            break


def heap_sort(lst):
    """Heap sort implementation in Python."""
    for i in range(len(lst), -1, -1):
        yield from _heapify(lst, len(lst), i)
    for i in range(len(lst) - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        yield (lst.copy(), {0, i}, {})
        yield from _heapify(lst, i, 0)
    yield (lst.copy(), {}, {})


def _heapify(lst, size, i):
    """Helper function for heap sort."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    yield (lst.copy(), {size, largest}, {})
    if left < size:
        if lst[largest] < lst[left]:
            largest = left
        yield (lst.copy(), {size, largest, left}, {})
    if right < size:
        if lst[largest] < lst[right]:
            largest = right
        yield (lst.copy(), {size, largest, right}, {})
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        yield (lst.copy(), {size, i, largest}, {})
        yield from _heapify(lst, size, largest)
