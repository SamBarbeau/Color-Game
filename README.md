# Color-Game

## Overview
This project is a color game inspired by an Instagram story filter saw a year or two ago. The game presents a grid of colors where one color is slightly different from the others. The player's task is to find and click on the different color before time runs out (5 seconds). I liked the concept of the game I saw on Instagram, but there were some parts I wanted to change up. For example, when I lost (chose the incorrect color) on Instagram's version, you just go to the end . This game is my attempt to implement those improvements.

## Features
- **Pyglet:** Uses Pyglet for game development and to interact with the game elements.
- **Game Mechanics:** Implements game mechanics to increase difficulty levels, track score, display RGB values of the missed color, etc.

## Requirements
- Python 3
- Pyglet

## Game Mechanics
The game mechanics developed for this color game (grid generation, color differentiation, mouse click handling, score tracking, level progression, and timer functionality) were inspired by the Instagram story filter game. The game starts with a grid of colors where one color is slightly different from the others. As the player's score increases, the game progresses to higher difficulty levels by increasing the grid size and decreasing the difference between the colors. If the player clicks on the wrong color or the time runs out, the game ends and the RGB values of the missed color are displayed.

Currently, the project is complete and fully functional. However, future improvements may be added based on user feedback and further testing... or if I get bored one day.

## Use the Program
To use the program, you need to have Python and Pyglet installed. You can install Pyglet with pip:
```bash
$ pip install pyglet
```

Enjoy the game and try to beat your high score!
