# === Sorting Algorithms ===
import Visualizer


def bubble_sort(screen, lst):
    """Bubble sort implementation in Python."""
    k = len(lst) - 1
    while k > 0:
        for i in range(k):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
            Visualizer.update_screen(screen, lst[:], {i, i + 1, k})
        k -= 1
    Visualizer.update_screen(screen, lst[:], {})


def selection_sort(screen, lst):
    """Selection sort implementation in Python."""
    for i in range(len(lst)):
        smallest = i
        for j in range(i, len(lst)):
            if lst[j] < lst[smallest]:
                smallest = j
            Visualizer.update_screen(screen, lst[:], {i, j, smallest})
        lst[smallest], lst[i] = lst[i], lst[smallest]
        Visualizer.update_screen(screen, lst[:], {i, smallest})
    Visualizer.update_screen(screen, lst[:], {})


def insertion_sort(screen, lst):
    """Insertion sort implementation in Python."""
    for i in range(0, len(lst)):
        key = lst[i]
        j = i
        while j > 0 and lst[j - 1] > key:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            Visualizer.update_screen(screen, lst[:], {i, j - 1, j})
            j -= 1
        lst[j], key = key, lst[j]
        Visualizer.update_screen(screen, lst[:], {i, j})
    Visualizer.update_screen(screen, lst[:], {})


def merge_sort(screen, lst):
    """Used to call merge sort."""
    _merge_sort(screen, lst, 0, len(lst) - 1)
    Visualizer.update_screen(screen, lst[:], {})


def _merge_sort(screen, lst, low, high):
    """Merge sort implementation in Python."""
    if low >= high:
        Visualizer.update_screen(screen, lst[:], {})
    else:
        mid = (low + high) // 2
        _merge_sort(screen, lst, low, mid)
        _merge_sort(screen, lst, mid + 1, high)
        _merge(screen, lst, low, mid, high)


def _merge(screen, lst, low, mid, high):
    """Helper function for merge sort."""
    merged = []
    i = low
    j = mid + 1
    while i < mid + 1 and j < high + 1:
        if lst[i] < lst[j]:
            merged.append(lst[i])
            Visualizer.update_screen(screen, lst[:], {i, j})
            i += 1
        else:
            merged.append(lst[j])
            Visualizer.update_screen(screen, lst[:], {i, j})
            j += 1
    while i < mid + 1:
        merged.append(lst[i])
        Visualizer.update_screen(screen, lst[:], {i})
        i += 1
    while j < high + 1:
        merged.append(lst[j])
        Visualizer.update_screen(screen, lst[:], {j})
        j += 1
    n = 0
    for k in range(low, high + 1):
        lst[k] = merged[n]
        Visualizer.update_screen(screen, lst[:], {k})
        n += 1


def quick_sort(screen, lst):
    """Used to call quick sort."""
    _quick_sort(screen, lst, 0, len(lst) - 1)
    Visualizer.update_screen(screen, lst[:], {})


def _quick_sort(screen, lst, low, high):
    """Quick sort implementation in Python."""
    if low >= high:
        Visualizer.update_screen(screen, lst[:], {})
    else:
        pivot = _partition(screen, lst, low, high)
        _quick_sort(screen, lst, low, pivot)
        _quick_sort(screen, lst, pivot + 1, high)


def _partition(screen, lst, low, high):
    """Helper function for quick sort."""
    pivot = lst[low]
    i = low
    j = high
    while i < j:
        while lst[i] < pivot:
            Visualizer.update_screen(screen, lst[:], {i, j, low})
            i += 1
        while lst[j] > pivot:
            Visualizer.update_screen(screen, lst[:], {i, j, low})
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
            Visualizer.update_screen(screen, lst[:], {i, j, low})
    return j


def heap_sort(screen, lst):
    """Heap sort implementation in Python."""
    for i in range(len(lst), -1, -1):
        _heapify(screen, lst, len(lst), i)
    for i in range(len(lst) - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        Visualizer.update_screen(screen, lst[:], {0, i})
        _heapify(screen, lst, i, 0)
    Visualizer.update_screen(screen, lst[:], {})


def _heapify(screen, lst, size, i):
    """Helper function for heap sort."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    Visualizer.update_screen(screen, lst[:], {size, largest})
    if left < size:
        if lst[largest] < lst[left]:
            largest = left
        Visualizer.update_screen(screen, lst[:], {size, largest, left})
    if right < size:
        if lst[largest] < lst[right]:
            largest = right
        Visualizer.update_screen(screen, lst[:], {size, largest, right})
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        Visualizer.update_screen(screen, lst[:], {size, largest, i})
        _heapify(screen, lst, size, largest)
