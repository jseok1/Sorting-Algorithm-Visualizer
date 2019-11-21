# === Sorting Algorithms Visualizer ===
import time

import pygame
import random
import SortingAlgorithms

# screen dimensions
WIDTH = 1024
HEIGHT = 576

# x-axis dimensions
X_WIDTH = 924
X_HEIGHT = 4

# problem size
SIZE = 250

# delay
DELAY = 1

# RGB colour values
WHITE = (255, 255, 255)
BLUE = (130, 215, 255)
RED = (255, 145, 145)
GREY = (240, 240, 240)


def run_visualizer():
    """Initialize and run this visualizer."""
    pygame.init()
    pygame.display.set_caption('Sorting Algorithm Visualizer')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    event_loop(screen)


def event_loop(screen):
    """Respond to events and update the visualizer."""
    lst = []
    reset(screen, lst)
    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset(screen, lst)
                elif event.key == pygame.K_1:
                    run_algorithm(screen, SortingAlgorithms.bubble_sort(lst))
                elif event.key == pygame.K_2:
                    run_algorithm(screen, SortingAlgorithms.selection_sort(lst))
                elif event.key == pygame.K_3:
                    run_algorithm(screen, SortingAlgorithms.insertion_sort(lst))
                elif event.key == pygame.K_4:
                    run_algorithm(screen, SortingAlgorithms.merge_sort(lst))
                elif event.key == pygame.K_5:
                    run_algorithm(screen, SortingAlgorithms.quick_sort(lst))
                elif event.key == pygame.K_6:
                    run_algorithm(screen, SortingAlgorithms.heap_sort(lst))


def reset(screen, lst):
    """Draw a random unsorted list onto the visualizer and return it."""
    lst.clear()
    lst.extend(random.sample(range(1, SIZE + 1), SIZE))   # problem size of 50
    update_visualizer(screen, lst, {})


def run_algorithm(screen, states):
    """Run the sorting algorithm and update the visualizer."""
    start = time.time()
    for state in states:
        update_visualizer(screen, state[0], state[1])
        pygame.event.pump()
        pygame.time.wait(DELAY)  # wait 15 ms
    end = time.time()
    print(end - start)


def update_visualizer(screen, lst, pivots):
    """Update the visualizer."""
    screen.fill(WHITE)  # clear screen
    draw_grid(screen)
    draw_rectangles(screen, lst, pivots)
    pygame.display.flip()  # update screen


def draw_rectangles(screen, lst, pivots):
    """Draw rectangles on the visualizer."""
    gap = X_WIDTH / (5 * len(lst) + 1)
    width = 4 * gap  # 4:1 ratio between rectangles and gap
    x = 50 + gap

    for i in range(len(lst)):
        height = 454 * (lst[i] / (SIZE + 1))
        y = HEIGHT - 62 - height
        if i in pivots:  # red rectangles
            pygame.draw.rect(screen, RED, pygame.Rect(x, y, width, height))
        else:  # blue rectangles
            pygame.draw.rect(screen, BLUE, pygame.Rect(x, y, width, height))
        x += width + gap


def draw_grid(screen):
    """Draw horizontal grid lines on the visualizer."""
    x = (WIDTH - X_WIDTH) / 2  # centers horizontally on screen
    y = HEIGHT - 60

    pygame.draw.rect(screen, GREY, pygame.Rect(x, y, X_WIDTH, X_HEIGHT))
    for i in range(5):  # draws 5 horizontal grid lines
        y -= 80
        pygame.draw.rect(screen, GREY, pygame.Rect(x, y, X_WIDTH, X_HEIGHT / 2))


if __name__ == '__main__':
    run_visualizer()
