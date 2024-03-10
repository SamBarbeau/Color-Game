import pyglet
from pyglet.shapes import BorderedRectangle

# Window size
window_width = 960
window_height = 540
grid_len = 350

# Create intro paragrph
intro_text = '''Welcome to the color game! Click on the start button to begin the game. The game will display a grid of cells, each with a random color. One of the cells will have a color that is slightly different from the rest. Click on the cell with the different color to score a point. The game will end if you click on the wrong cell. Good luck!

Level 1: 2x2 grid
Level 2: 3x3 grid (harder color diff)
Level 3: 4x4 grid
Level 4: 4x4 grid (harder color diff)
Level 5: 5x5 grid'''

intro_game_back = BorderedRectangle(window_width // 2 + grid_len // 2 + 15, window_height // 2 - 140, 275, 275, color=(0, 0, 0), border=5, border_color=(100, 100, 100))
intro = pyglet.text.Label(intro_text,
                            font_name='Verdana', font_size=10, width=255, multiline=True,
                            x=window_width // 2 + grid_len // 2 + 25, y=window_height // 2,
                            anchor_x='left', anchor_y='center', color=(255, 255, 255, 255))

# Create the start,reset buttons
start_button = BorderedRectangle(window_width // 2 - 100, window_height - 72.5, 100, 50, color=(0, 120, 215), border=2.5, border_color=(0, 0, 0))
start_label = pyglet.text.Label('start', font_name='Verdana', font_size=13,
                                    x=start_button.x + start_button.width // 2, y=start_button.y + start_button.height // 2,
                                    anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))

reset_button = BorderedRectangle(window_width // 2, window_height - 72.5, 100, 50, color=(0, 120, 215), border=2.5, border_color=(0, 0, 0))
reset_label = pyglet.text.Label('reset', font_name='Verdana', font_size=13,
                                    x=reset_button.x + reset_button.width // 2, y=reset_button.y + reset_button.height // 2,
                                    anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))

# Create a score counter
score_back = BorderedRectangle(87.5, 270, 130, 50, color=(0, 120, 215), border=2.5, border_color=(0, 0, 0))
score_label = pyglet.text.Label('score: 0', font_name='Verdana', font_size=13,
                                    x=score_back.x + score_back.width // 2, y=score_back.y + score_back.height // 2,
                                    anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))

high_score_back = BorderedRectangle(87.5, 220, 130, 50, color=(0, 120, 215), border=2.5, border_color=(0, 0, 0))
high_score_label = pyglet.text.Label('highscore: 0', font_name='Verdana', font_size=13,
                                        x=high_score_back.x + high_score_back.width // 2, y=high_score_back.y + high_score_back.height // 2,
                                        anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))

# Level label
level_label = pyglet.text.Label('Level: 1', font_name='Verdana', font_size=20,
                                    x=window_width // 2 + grid_len // 2 + 152.5, y=intro_game_back.y + intro_game_back.height * (3/4),
                                    anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))

# Timer label
timer_label = pyglet.text.Label('Time: 5 sec', font_name='Verdana', font_size=20,
                                    x=window_width // 2 + grid_len // 2 + 152.5, y=intro_game_back.y + intro_game_back.height * (1/4),
                                    anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))

# endgame info
end_game_back = BorderedRectangle(722.5, 120, 170, 300, color=(0, 120, 215), border=5, border_color=(0, 0, 0))
end_game_label = pyglet.text.Label('Game Over:', font_name='Verdana', font_size=15, bold=True,
                                    x=end_game_back.x + end_game_back.width // 2, y=end_game_back.y + end_game_back.height - 20,
                                    anchor_x='center', anchor_y='top', color=(255, 255, 255, 255))

different_color_label = pyglet.text.Label('Different Color:', font_name='Verdana', font_size=13,
                                            x=end_game_back.x + end_game_back.width // 2, y=end_game_back.y + end_game_back.height - 80,
                                            anchor_x='center', anchor_y='top', color=(255, 255, 255, 255))

diff_value_label = pyglet.text.Label('(R,G,B)', font_name='Verdana', font_size=13,
                                        x=end_game_back.x + end_game_back.width // 2, y=end_game_back.y + end_game_back.height - 110,
                                        anchor_x='center', anchor_y='top', color=(255, 255, 255, 255))

rest_color_label = pyglet.text.Label('Rest of Colors:', font_name='Verdana', font_size=13,
                                        x=end_game_back.x + end_game_back.width // 2, y=end_game_back.y + end_game_back.height - 180,
                                        anchor_x='center', anchor_y='top', color=(255, 255, 255, 255))

rest_value_label = pyglet.text.Label('(R,G,B)', font_name='Verdana', font_size=13,
                                        x=end_game_back.x + end_game_back.width // 2, y=end_game_back.y + end_game_back.height - 210,
                                        anchor_x='center', anchor_y='top', color=(255, 255, 255, 255))