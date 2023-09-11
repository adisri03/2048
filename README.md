# 2048
![Python](https://img.shields.io/badge/Python%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)



## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
   - [How to Play](#usage)


## Introduction
This is a simple implementation of the popular 2048 game in Python. In the game, you need to slide tiles in four directions (up, down, left, right) and combine tiles with the same number to reach the 2048 tile. The game board is a 4x4 grid, and your goal is to achieve the highest score possible by combining tiles.



## Getting Started
1. Clone or download the repository to your local machine.
   
2. Open a terminal and navigate to the directory containing the game code.\
   
3. Run the game by executing the following command:
   ```bash
   python 2048.py
   ```
## How to Play
1.Use the following keys to make moves:

  'W' or 'w' to move up
  
  'S' or 's' to move down
  
  'A' or 'a' to move left
  
  'D' or 'd' to move right
  
2.When two tiles with the same number touch, they merge into one tile with a value equal to the sum of their values.

3.After each move, a new tile with a value of 2 will appear in an empty spot on the board.

4.Your objective is to reach the 2048 tile by combining tiles strategically.

5. The game can end in one of the following ways:
   
    You reach the 2048 tile, and you win the game.
   
    There are no empty spaces left on the board, and no adjacent tiles can be merged. In this case, you lose the game.
