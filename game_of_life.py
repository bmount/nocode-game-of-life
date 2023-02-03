
# Conway's Game of Life

# Create a 2D array of cells, each cell is either alive or dead
# The state of the cells changes over time according to the following rules:
# 1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
# 2. Any live cell with two or three live neighbours lives on to the next generation.

# Render to a pygame window

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 10

# This sets the margin between each cell
MARGIN = 1

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [510, 510]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Conway's Game of Life")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

BOARD_DIM = 50

# Find the number of live neighbors for a given cell
def get_live_neighbors(board, row, col):
    live_neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if row + i < 0 or row + i >= BOARD_DIM:
                continue
            if col + j < 0 or col + j >= BOARD_DIM:
                continue
            if board[row + i][col + j] == 1:
                live_neighbors += 1
    return live_neighbors

def create_game():
    new_board = []
    for row in range(BOARD_DIM):
        new_board.append([])
        for column in range(BOARD_DIM):
            new_board[row].append(0)
    for row in range(BOARD_DIM):
        for column in range(BOARD_DIM):
            if random.randint(0, 1) == 1:
                new_board[row][column] = 1
    return new_board

def update_game(board):
    new_board = []
    for row in range(BOARD_DIM):
        new_board.append([])
        for column in range(BOARD_DIM):
            new_board[row].append(0)
    for row in range(BOARD_DIM):
        for column in range(BOARD_DIM):
            live_neighbors = get_live_neighbors(board, row, column)
            if board[row][column] == 1:
                if live_neighbors < 2:
                    new_board[row][column] = 0
                elif live_neighbors == 2 or live_neighbors == 3:
                    new_board[row][column] = 1
                elif live_neighbors > 3:
                    new_board[row][column] = 0
            else:
                if live_neighbors == 3:
                    new_board[row][column] = 1
    return new_board

# randomly inject some live cells
def inject_cells(board):
    for row in range(BOARD_DIM):
        for column in range(BOARD_DIM):
            if random.randint(0, 1) == 1:
                board[row][column] = 1
    return board

# -------- Main Program Loop -----------
board = create_game()
n_gens = 3
while not done:
    n_gens += 1
    # update the board
    board = update_game(board)
    # display the board

    if not n_gens % 100:
        board = inject_cells(board)
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(BLACK)
    # Show the main game board:
    for row in range(BOARD_DIM):
        for column in range(BOARD_DIM):
            color = WHITE
            if board[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + WIDTH) * row + MARGIN,
                              WIDTH,
                              WIDTH])

    # Go ahead and update the screen with what we've drawn. 
    pygame.display.flip()

    # display each generation for 10 ms
    pygame.time.wait(10)
    # Limit to 60 frames per second
    clock.tick(60)
