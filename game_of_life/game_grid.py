import random
from copy import deepcopy
from dataclasses import dataclass

from .cell import Cell
from .enums import CellState


@dataclass
class GameGrid:
    """Class to represent the game grid."""
    grid: list[list[Cell]] # The grid game, a list of lists of cells
    __gen_grid: list[list[Cell]] # A copy of the grid game, used to update the next generation
    __old_gen_grid: list[list[Cell]] # A copy of the grid game, used to check if the grid can change or not on the futures generations (stabilized)
    size: (int, int) # The size of the grid game
    generation: int = 0 # The current generation
    stabilized: bool = False # If the grid can change or not on the futures generations (stabilized)
    starting_alive_probability: float = 0.5 # The probability of life spawn when you init the grid randomly

    def __init__(self, size: (int, int)) -> None:
        self.size = size
        self.grid = [[Cell() for _ in range(size[1])] for _ in range(size[0])]  # TODO: Check if this is correct
        self.__gen_grid = deepcopy(self.grid)
        self.__old_gen_grid = deepcopy(self.grid)

    def init_grid_random(self, alive_probability: float = 0.5) -> None:
        """Initialize the grid with random values."""
        self.starting_alive_probability = alive_probability
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                if random.random() < self.starting_alive_probability:
                    self.grid[x][y].cell_state = CellState.ALIVE

    def get_neighbors(self, x: int, y: int) -> list[Cell]:
        """Get the neighbors of a cell."""
        neighbors = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if (dx == 0 and dy == 0) or not (0 <= nx < self.size[0] and 0 <= ny < self.size[1]):
                    continue # Skip the cell itself and out of bounds cells
                neighbors.append(self.__gen_grid[nx][ny])
        return neighbors

    def update_next_generation(self) -> None:
        """update the next generation of the game grid."""
        # Check if the grid can change or not on the futures generations (stabilized)
        self.is_stabilized()

        # Use a copy of the grid to update the next generation
        self.__gen_grid = deepcopy(self.grid)

        for x, _ in enumerate(range(self.size[0])):
            for y, _ in enumerate(range(self.size[1])):
                neighbors = self.get_neighbors(x, y)
                self.grid[x][y].set_next_state(neighbors)
        self.generation += 1

    def is_stabilized(self) -> bool:
        """Check if the grid can change or not on the futures generations (stabilized)."""
        if self.__old_gen_grid == self.grid:
            self.stabilized = True
        self.__old_gen_grid = deepcopy(self.__gen_grid)
        return self.stabilized

    def print_grid(self) -> None:
        """Print the game grid."""
        for x in range(self.size[0]):
            print(''.join("⬜" if self.grid[x][y].cell_state == CellState.ALIVE else "⬛" for y in range(self.size[1])))

    def print_grid_info(self) -> None:
        """Print the game grid info (size, stabilized and starting_alive_probability)."""
        print(f"Generation: {self.generation}, size: {self.size[0]}x{self.size[1]}, stabilized: {self.stabilized}, "
              f"starting_alive_probability: {self.starting_alive_probability}")