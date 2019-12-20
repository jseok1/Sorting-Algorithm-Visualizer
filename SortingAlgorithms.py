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
        yield (lst.copy(), {lst.index(key), j}, {})
    yield (lst.copy(), {}, {})


def merge_sort(lst):
    """Merge sort implementation in Python."""
    yield from _merge_sort(lst, 0, len(lst) - 1)
    yield (lst.copy(), {}, {})


def _merge_sort(lst, low, high):
    """Merge sort implementation in Python."""
    if low >= high:
        yield (lst.copy(), {}, {n for n in range(low, high + 1)})
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
    while i <= mid and j <= high:
        if lst[i] < lst[j]:
            merged.append(lst[i])
            yield (lst.copy(), {i, j}, {n for n in range(low, high + 1)})
            i += 1
        else:
            merged.append(lst[j])
            yield (lst.copy(), {i, j}, {n for n in range(low, high + 1)})
            j += 1
    while i <= mid:
        merged.append(lst[i])
        yield (lst.copy(), {i}, {n for n in range(low, high + 1)})
        i += 1
    while j <= high:
        merged.append(lst[j])
        yield (lst.copy(), {j}, {n for n in range(low, high + 1)})
        j += 1
    for k in range(high - low + 1):
        lst[low + k] = merged[k]
        yield (lst.copy(), {low + k}, {n for n in range(low, high + 1)})


def quick_sort(lst):
    """Quick sort implementation in Python."""
    yield from _quick_sort(lst, 0, len(lst) - 1)
    yield (lst.copy(), {}, {})


def _quick_sort(lst, low, high):
    """Quick sort implementation in Python."""
    if low >= high:
        yield (lst.copy(), {}, {n for n in range(low, high + 1)})
    else:
        pivot = -1
        for p in _partition(lst, low, high):
            yield p
            pivot = max(p[1])
        yield from _quick_sort(lst, low, pivot)
        yield from _quick_sort(lst, pivot + 1, high)


def _partition(lst, low, high):
    """Helper function for quick sort."""
    pivot = lst[low]
    i = low + 1
    j = high
    while True:
        while i <= j and lst[i] < pivot:
            yield (lst.copy(), {i, j, low}, {n for n in range(low, high + 1)})
            i += 1
        while i <= j and lst[j] > pivot:
            yield (lst.copy(), {i, j, low}, {n for n in range(low, high + 1)})
            j -= 1
        if i > j:
            break
        lst[i], lst[j] = lst[j], lst[i]
        yield (lst.copy(), {i, j, low}, {n for n in range(low, high + 1)})
    lst[low], lst[j] = lst[j], lst[low]
    yield (lst.copy(), {j, low}, {n for n in range(low, high + 1)})


def heap_sort(lst):
    """Heap sort implementation in Python."""
    for i in range(len(lst), -1, -1):
        yield from _heapify(lst, len(lst), i)
    for i in range(len(lst) - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        yield (lst.copy(), {0, i}, {})
        yield from _heapify(lst, i, 0)
    yield (lst.copy(), {}, {})


def _heapify(lst, n, i):
    """Helper for heap sort."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and lst[largest] < lst[left]:
        largest = left
        yield (lst.copy(), {i, largest, n}, {j for j in range(i, n)})
    if right < n and lst[largest] < lst[right]:
        largest = right
        yield (lst.copy(), {i, largest, n}, {j for j in range(i, n)})
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        yield (lst.copy(), {i, largest, n}, {j for j in range(i, n)})
        yield from _heapify(lst, n, largest)
