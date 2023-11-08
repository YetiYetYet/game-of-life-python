from copy import deepcopy
from dataclasses import dataclass
import numpy as np

from .cell import Cell
from .cell_state import CellState


@dataclass
class GameGrid:
    """Class to represent the game grid."""
    grid: list[list[Cell]]
    __gen_grid: list[list[Cell]]
    __old_gen_grid: list[list[Cell]]
    size: (int, int)
    generation: int
    stabilized: bool = False
    starting_alive_probability: float = 0.5

    def __init__(self, size: (int, int)):
        self.size = size
        self.generation = 0
        self.grid = [[Cell() for _ in range(size[1])] for _ in range(size[0])]  # TODO: Check if this is correct
        self.__gen_grid = deepcopy(self.grid)
        self.__old_gen_grid = deepcopy(self.grid)

    def init_grid_random(self, alive_probability: float = 0.5):
        """Initialize the grid with random values."""
        self.starting_alive_probability = alive_probability
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                if np.random.random() < self.starting_alive_probability:
                    self.grid[x][y].cell_state = CellState.ALIVE

    def set_cell(self, x: int, y: int, cell: Cell):
        self.grid[x][y] = cell

    def get_neighbors(self, x: int, y: int) -> list[Cell]:
        """Get the neighbors of a cell."""
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    # Skip the cell itself
                    continue
                if x + i < 0 or x + i >= self.size[0]:
                    # Skip out of bounds cells
                    continue
                if y + j < 0 or y + j >= self.size[1]:
                    # Skip out of bounds cells
                    continue
                neighbors.append(self.__gen_grid[x + i][y + j])
        return neighbors

    def update_next_generation(self):
        """update the next generation of the game grid."""
        if self.__old_gen_grid == self.grid:
            self.stabilized = True
        self.__old_gen_grid = deepcopy(self.__gen_grid)
        self.__gen_grid = deepcopy(self.grid)
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                cell = self.grid[x][y]
                neighbors = self.get_neighbors(x, y)
                cell.set_next_state(neighbors)
        self.generation += 1

    def print_grid(self):
        """Print the game grid."""
        print(f"Generation: {self.generation}, size: {self.size[0]}x{self.size[1]}, stabilized: {self.stabilized}, "
              f"starting_alive_probability: {self.starting_alive_probability}")
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                cell = self.grid[x][y]
                if cell.cell_state == CellState.ALIVE:
                    print("⬜", end="")
                else:
                    print("⬛", end="")
            print()
