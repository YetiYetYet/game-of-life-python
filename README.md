# Conway's Game of Life in Python

This project is a Python implementation of Conway's Game of Life, 
a cellular automaton devised by the British mathematician John Horton Conway in 1970. 
The game is a zero-player game, meaning that its evolution is determined by its initial
state, requiring no further input. One interacts with the Game of Life by creating an 
initial configuration and observing how it evolves.

## Introduction

The Game of Life is not your typical computer game. 
It consists of a grid of cells which, based on a few mathematical rules, 
can live, die or multiply. Depending on the initial conditions, 
the cells form various patterns throughout the course of the game.

The packages is available on PyPI: https://pypi.org/project/game-of-life-YETIYETYET/

## Rules of the Game

The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead. Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

1. **Underpopulation**: A live cell with fewer than two live neighbours dies.
2. **Stasis**: A live cell with two or three live neighbours lives on to the next generation.
3. **Overpopulation**: A live cell with more than three live neighbours dies.
4. **Reproduction**: A dead cell with exactly three live neighbours becomes a live cell.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed, live or dead; births and deaths occur simultaneously.

## Sample of the output project
![Demo GameOfLife](docs/demo.gif)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before running this project, you need to have Python installed on your system (Python 3.12 is recommended). 
You can download Python from the official website:
https://www.python.org/downloads/

### Installing
Clone the repository to your local machine:
git clone https://github.com/YetiYetYet/game-of-life-python.git

Install the required dependencies :
``pip install -r requirements.txt``

### Running the Game

To run the game, execute the following command in the terminal:
``python main.py``

## Usage

1. Run the main script.
2. Follow the instructions in the terminal. It will ask to enter a size for the grid, a starting alive probability. 
By default, if you enter nothing, the size will be 10x40 and the starting alive probability will be 0.5.
3. Watch the game evolve in your terminal.

## Authors

* **YetiYetYet** - [YetiYetYet](https://github.com/YetiYetYet)

## Questions/Contact

If you have any questions or concerns, please reach out to me at alexisbehier22@gmail.com.
