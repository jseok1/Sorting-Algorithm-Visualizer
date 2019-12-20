# === Sorting Algorithms Visualizer ===
import time
import pygame
import random

import SortingAlgorithms

# screen dimensions
WIDTH = 1024
HEIGHT = 576

# problem size
SIZE = 20  # recommended: 200

# delay
DELAY = 250  # recommended: 5

# RGB colour values
WHITE = (255, 255, 255)
BLUE = (130, 215, 255)
RED = (255, 145, 145)
ORANGE = (255, 210, 160)
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
    """Draw a random unsorted list onto the visualizer."""
    lst.clear()
    lst.extend([0] * SIZE)
    temp = random.sample(range(1, SIZE + 1), SIZE)
    for i in range(len(temp)):
        lst[i] = temp[i]
        update_visualizer(screen, lst, {}, {})
        pygame.event.pump()
        pygame.time.wait(1)


def run_algorithm(screen, states):
    """Run the sorting algorithm and update the visualizer."""
    start = time.time()
    for state in states:
        update_visualizer(screen, state[0], state[1], state[2])
        pygame.event.pump()
        pygame.time.wait(DELAY)
    end = time.time()
    print(end - start)


def update_visualizer(screen, lst, primary, secondary):
    """Update the visualizer with a new frame."""
    screen.fill(WHITE)  # clear screen
    draw_lines(screen)
    draw_rectangles(screen, lst, primary, secondary)
    pygame.display.flip()  # update screen


def draw_rectangles(screen, lst, primary, secondary):
    """Draw rectangles on the visualizer."""
    gap = (WIDTH - 100) / (5 * SIZE + 1)
    width = 4 * gap  # 4:1 ratio between rectangles and gap
    x = 50 + gap
    for i in range(len(lst)):
        height = (HEIGHT - 100) * (lst[i] / SIZE)
        y = HEIGHT - 52 - height
        if height != 0:
            rect = pygame.Rect(x, y, width, height)
            if i in primary:  # red rectangles
                pygame.draw.rect(screen, RED, rect)
            elif i in secondary:  # orange rectangles
                pygame.draw.rect(screen, ORANGE, rect)
            else:  # blue rectangles
                pygame.draw.rect(screen, BLUE, rect)
        x += width + gap


def draw_lines(screen):
    """Draw reference lines on the visualizer."""
    x = 50
    y = HEIGHT - 50
    pygame.draw.rect(screen, GREY, pygame.Rect(x, y, WIDTH - 100, 4))
    for i in range(5):
        y -= HEIGHT * 0.15
        pygame.draw.rect(screen, GREY, pygame.Rect(x, y, WIDTH - 100, 2))
