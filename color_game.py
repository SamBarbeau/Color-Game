import pyglet
from pyglet.shapes import Rectangle, BorderedRectangle
import random
import numpy as np
from items import *

# Window size
window_width = 960
window_height = 540

# Window creation
window = pyglet.window.Window(window_width, window_height)

# Grid size
grid_size = 2
cell_size = 350 // grid_size

# Variable to store the different colored cell
different_cell = None

# Load in high score cache
try:
    high_score_cache = np.load('high_score_cache.npy', allow_pickle=True).item()
    high_score = high_score_cache['high_score']
    high_score_label.text = f'highscore: {high_score}'
except:
    high_score_cache = {}
    high_score = 0

# Variables to store the game state
game_started = False
game_over = False
score = 0
color_diff = 20
level = 1
time_limit = 4

# Variables from items. started so can loop over later
labels = [start_button,start_label,reset_button,reset_label,score_back,score_label,high_score_back,high_score_label]
end_game_info = [end_game_back,end_game_label,different_color_label,diff_value_label,rest_color_label,rest_value_label]
game_info = [intro_game_back,level_label,timer_label]

# Grid creation
grid = [[None for _ in range(grid_size)] for _ in range(grid_size)]

grid_space = Rectangle(window_width // 2 - cell_size * grid_size // 2,
                        window_height // 2 - cell_size * grid_size // 2,
                        cell_size * grid_size, cell_size * grid_size,
                        color=(255, 255, 255))


def color_grid():
    global different_cell
    window.clear()

    # Generate random color
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    for i in range(grid_size):
        for j in range(grid_size):
            x = window_width // 2 - cell_size * grid_size // 2 + i * cell_size
            y = window_height // 2 - cell_size * grid_size // 2 + j * cell_size

            # Set cell
            grid[i][j] = BorderedRectangle(x, y, cell_size, cell_size, color=color, border=2.5, border_color=(0, 0, 0))

    # Select a random cell and a random color component to be off by a bit
    different_cell = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
    different_color = list(grid[different_cell[0]][different_cell[1]].color)

    # always change the largest componenet (sometimes changing the smallest component, even by a lot, is hard to see)
    color_component = different_color.index(max(different_color[:-1]))

    if 255 - (different_color[color_component] + color_diff) < 0:
        different_color[color_component] -= color_diff
    else:
        different_color[color_component] += color_diff
    grid[different_cell[0]][different_cell[1]].color = tuple(different_color)

def default_grid():
    for i in range(grid_size):
        for j in range(grid_size):
            x = window_width // 2 - cell_size * grid_size // 2 + i * cell_size
            y = window_height // 2 - cell_size * grid_size // 2 + j * cell_size

            # Set cell
            grid[i][j] = BorderedRectangle(x, y, cell_size, cell_size, color=(255, 255, 255), border=2.5, border_color=(0, 0, 0))


@window.event
def on_draw():
    window.clear()
    if not game_started:
        default_grid()
        intro_game_back.draw()
        intro.draw()

    for i in range(grid_size):
        for j in range(grid_size):
            # Draw cell
            grid[i][j].draw()

    # Draw buttons/labels from items.py
    for item in labels:
        item.draw()
    
    if game_over:
        for item in end_game_info:
            item.draw()
    elif game_started:
        level_label.text = f'Level: {level}'
        for item in game_info:
            item.draw()

# This function is need for when moving to next level (or reset)
def level_up(new_level, new_color_diff, new_grid_size):
    global grid_size, grid, cell_size, level, color_diff

    grid_size = new_grid_size
    level = new_level
    color_diff = new_color_diff
    grid = [[None for _ in range(grid_size)] for _ in range(grid_size)]
    cell_size = 350 // grid_size # size of grid should be 350x350

def start_game():
    global game_started, time_limit, score, game_over
    game_started = True
    game_over = False

    level_up(1, 20, 2) # reset level, color_diff, grid_size

    score = 0
    score_label.text = f'score: {score}'

    time_limit = 4  # Reset the time limit
    pyglet.clock.schedule_interval(update_timer, 0.1)  # Start the timer

def end_game():
    global game_over

    game_over = True

    # show the different color
    grid[different_cell[0]][different_cell[1]].border_color = (255, 255, 255)

    # update RGB values for end game info
    diff_value_label.text = f'{grid[different_cell[0]][different_cell[1]].color[:-1]}'

    if different_cell == (0, 0):
        rest_value_label.text = f'{grid[0][1].color[:-1]}'
    else:
        rest_value_label.text = f'{grid[0][0].color[:-1]}'

    pyglet.clock.unschedule(update_timer)  # Stop the timer

    # Update high score cache
    high_score_cache['high_score'] = high_score
    np.save('high_score_cache.npy', high_score_cache)

# Timer function
def update_timer(dt):
    global time_limit
    if game_started and not game_over:
        time_limit -= 0.1
        timer_label.text = f'Time: {round(time_limit,1)} sec'
        if time_limit <= 0:
            end_game()

@window.event
def on_mouse_press(x, y, button, modifiers):
    global game_started, score, game_over, high_score, level, grid_size, color_diff, grid, time_limit

    if (x,y) in start_button:
        start_game()
        color_grid()

    elif (x,y) in reset_button:
        game_started = False
        game_over = False
        score = 0
        score_label.text = f'score: {score}'
        level_up(1, 20, 2) # reset level, color_diff, grid_size

    elif (x,y) in grid_space and game_started and not game_over:
        # need this so no "double clicks" happen
        found_cell = False
        for i in range(grid_size):
            for j in range(grid_size):
                if (x,y) in grid[i][j] and different_cell == (i, j):
                    found_cell = True

                    score += 1
                    high_score = max(score, high_score)
                    score_label.text = f'score: {score}'
                    high_score_label.text = f'highscore: {high_score}'

                    if score == 5:
                        level_up(2, 15, 3)
                    elif score == 10:
                        level_up(3, 15, 4)
                    elif score == 20:
                        level_up(4, 10, 4)
                    elif score == 30:
                        level_up(5, 10, 5)

                    color_grid()

                    time_limit = 4  # Reset the time limit
                    break
                elif (x,y) in grid[i][j] and different_cell != (i, j):
                    found_cell = True

                    end_game()

                    grid[i][j].border_color = (255, 0, 0) # highlight the wrongly clicked cell
                    break

            if found_cell:
                break

@window.event
def on_mouse_motion(x, y, dx, dy):
    # Change color of buttons when hovered over
    if (x, y) in start_button:
        start_button.color = (0, 150, 255)
    else:
        start_button.color = (0, 120, 215)

    if (x, y) in reset_button:
        reset_button.color = (0, 150, 255)
    else:
        reset_button.color = (0, 120, 215)

pyglet.app.run()