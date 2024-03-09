import pyglet
from pyglet.shapes import Rectangle, BorderedRectangle
import random
from items import *

### todo: add a level system to increase difficulty
###         - increase grid size
###         - decrease color difference
###
###       add timer to game

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

# Variables to store the game state
game_started = False
game_over = False
score = 0
high_score = 0
color_diff = 30
level = 1

# Variables from items. started so can loop over later
labels = [start_button,start_label,reset_button,reset_label,score_back,score_label,high_score_back,high_score_label]
end_game_info = [end_game_back,end_game_label,different_color_label,diff_value_label,rest_color_label,rest_value_label]
game_info = [intro_game_back,level_label]

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
    color_component = random.randint(0, 2)

    different_color = list(grid[different_cell[0]][different_cell[1]].color)
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

@window.event
def on_mouse_press(x, y, button, modifiers):
    global game_started, score, game_over, high_score, level, grid_size, color_diff, grid

    if (x,y) in start_button:
        game_started = True
        score = 0
        game_over = False
        level_up(1, 30, 2) # reset level, color_diff, grid_size
        color_grid()
    if (x,y) in reset_button:
        game_started = False
        score = 0
        game_over = False
        level_up(1, 30, 2) # reset level, color_diff, grid_size
    elif (x,y) in grid_space and game_started and not game_over:
        for i in range(grid_size):
            for j in range(grid_size):
                if (x,y) in grid[i][j] and different_cell == (i, j):
                    score += 1
                    high_score = max(score, high_score)
                    score_label.text = f'score: {score}'
                    high_score_label.text = f'highscore: {high_score}'

                    if score == 5:
                        level_up(2, 25, 3)
                    elif score == 10:
                        level_up(3, 25, 4)
                    elif score == 20:
                        level_up(4, 20, 4)
                    elif score == 30:
                        level_up(5, 20, 5)

                    color_grid()
                    break
                elif (x,y) in grid[i][j] and different_cell != (i, j):
                    game_over = True
                    grid[different_cell[0]][different_cell[1]].border_color = (255, 255, 255)
                    diff_value_label.text = f'{grid[different_cell[0]][different_cell[1]].color[:-1]}'
                    rest_value_label.text = f'{grid[i][j].color[:-1]}'
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