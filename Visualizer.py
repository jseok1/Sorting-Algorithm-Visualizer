# === Sorting Algorithms Visualizer ===
import pygame
import random

import SortingAlgorithms

# screen dimensions
WIDTH = 1024
HEIGHT = 576

# problem size
SIZE = 75

# delay
DELAY = 10

# RGB colour values
WHITE = (255, 255, 255)
BLUE = (120, 225, 255)
PURPLE = (125, 170, 255)
RED = (255, 110, 110)
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
                    SortingAlgorithms.bubble_sort(screen, lst)
                elif event.key == pygame.K_2:
                    SortingAlgorithms.selection_sort(screen, lst)
                elif event.key == pygame.K_3:
                    SortingAlgorithms.insertion_sort(screen, lst)
                elif event.key == pygame.K_4:
                    SortingAlgorithms.merge_sort(screen, lst)
                elif event.key == pygame.K_5:
                    SortingAlgorithms.quick_sort(screen, lst)
                elif event.key == pygame.K_6:
                    SortingAlgorithms.heap_sort(screen, lst)
    pygame.quit()


def reset(screen, lst):
    """Draw a random unsorted list onto the visualizer."""
    lst.clear()
    lst.extend([0] * SIZE)
    temp = random.sample(range(1, SIZE + 1), SIZE)
    for i in range(SIZE):
        lst[i] = temp[i]
        update(screen, lst, {})


def update(screen, lst, accent):
    """Update the visualizer with a new frame."""
    screen.fill(WHITE)  # clear screen
    draw_lines(screen)
    draw_rectangles(screen, lst, accent)
    pygame.display.flip()  # update screen
    pygame.event.pump()
    pygame.time.wait(DELAY)


def draw_rectangles(screen, lst, accent):
    """Draw rectangles on the visualizer."""
    gap = (WIDTH - 100) / (11 * SIZE + 1)
    width = 10 * gap  # 10:1 ratio between rectangles and gap
    x = 50 + gap
    for i in range(len(lst)):
        height = (HEIGHT - 100) * (lst[i] / SIZE)
        y = HEIGHT - 52 - height
        if height != 0:
            rect = pygame.Rect(x, y, width, height)
            if i in accent:  # red rectangles
                pygame.draw.rect(screen, RED, rect)
            else:  # blue rectangles
                red = BLUE[0] + (PURPLE[0] - BLUE[0]) * (lst[i] / SIZE)
                green = BLUE[1] + (PURPLE[1] - BLUE[1]) * (lst[i] / SIZE)
                blue = BLUE[2] + (PURPLE[2] - BLUE[2]) * (lst[i] / SIZE)
                pygame.draw.rect(screen, (red, green, blue), rect)
        x += width + gap


def draw_lines(screen):
    """Draw reference lines on the visualizer."""
    x = 50
    y = HEIGHT - 50
    pygame.draw.rect(screen, GREY, pygame.Rect(x, y, WIDTH - 100, 4))
    for i in range(5):
        y -= HEIGHT * 0.15
        pygame.draw.rect(screen, GREY, pygame.Rect(x, y, WIDTH - 100, 2))
