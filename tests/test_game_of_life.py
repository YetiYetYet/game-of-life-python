import unittest
from src.game_of_life import GameGrid
from src.game_of_life import Cell
from src.game_of_life import CellState


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.game_grid = GameGrid((6, 6))
        self.excepted_game_grid = GameGrid((6, 6))
        self.print_debug = False

    def test_underpopulation(self):
        # A cell with fewer than 2 live neighbors should die (underpopulation)
        self.game_grid.grid = [
            [Cell(CellState.DEAD) for _ in range(6)],
            [Cell(CellState.DEAD), Cell(CellState.ALIVE), Cell(CellState.DEAD)] + [Cell(CellState.DEAD) for _ in range(3)],
            [Cell(CellState.ALIVE), Cell(CellState.DEAD)] + [Cell(CellState.DEAD) for _ in range(4)],
            [Cell(CellState.DEAD) for _ in range(6)],
            [Cell(CellState.DEAD) for _ in range(6)],
            [Cell(CellState.DEAD) for _ in range(6)]
        ]
        if self.print_debug:
            print("Initial grid")
            self.game_grid.print_grid()
        self.game_grid.update_next_generation()
        if self.print_debug:
            print("Updated grid")
            self.game_grid.print_grid()
        self.excepted_game_grid.grid = [[Cell(CellState.DEAD) for _ in range(6)] for _ in range(6)]  # All cells should be dead
        if self.print_debug:
            print("Excepted grid")
            self.excepted_game_grid.print_grid()
        self.assertEqual(self.game_grid.grid, self.excepted_game_grid.grid)

    def test_overcrowding(self):
        # A cell with more than 3 live neighbors should die (overcrowding)
        self.game_grid.grid = [
            [Cell(CellState.ALIVE), Cell(CellState.ALIVE), Cell(CellState.DEAD)] + [Cell(CellState.DEAD) for _ in range(3)],
            [Cell(CellState.ALIVE), Cell(CellState.ALIVE), Cell(CellState.ALIVE)] + [Cell(CellState.DEAD) for _ in range(3)],
            [Cell(CellState.ALIVE), Cell(CellState.ALIVE), Cell(CellState.DEAD)] + [Cell(CellState.DEAD) for _ in range(3)],
            [Cell(CellState.DEAD) for _ in range(6)],
            [Cell(CellState.DEAD) for _ in range(6)],
            [Cell(CellState.DEAD) for _ in range(6)]
        ]
        if self.print_debug:
            print("Initial grid")
            self.game_grid.print_grid()
        self.game_grid.update_next_generation()
        if self.print_debug:
            print("Updated grid")
            self.game_grid.print_grid()
        self.excepted_game_grid.grid = [
            [Cell(CellState.ALIVE), Cell(CellState.DEAD), Cell(CellState.ALIVE)] + [Cell(CellState.DEAD) for _ in range(3)],
            [Cell(CellState.DEAD), Cell(CellState.DEAD), Cell(CellState.ALIVE)] + [Cell(CellState.DEAD) for _ in range(3)],
            [Cell(CellState.ALIVE), Cell(CellState.DEAD), Cell(CellState.ALIVE)] + [Cell(CellState.DEAD) for _ in range(3)],
            [Cell(CellState.DEAD) for _ in range(6)],
            [Cell(CellState.DEAD) for _ in range(6)],
            [Cell(CellState.DEAD) for _ in range(6)]
        ]
        if self.print_debug:
            print("Excepted grid")
            self.excepted_game_grid.print_grid()
        self.assertEqual(self.game_grid.grid, self.excepted_game_grid.grid)

    def test_survival(self):
        # A cell with 2 or 3 live neighbors should survive
        self.game_grid.grid = [
            [Cell(CellState.DEAD), Cell(CellState.ALIVE), Cell(CellState.DEAD)] + [Cell(CellState.DEAD) for _ in range(3)],
            [Cell(CellState.ALIVE), Cell(CellState.ALIVE), Cell(CellState.ALIVE)] + [Cell(CellState.DEAD) for _ in range(3)],
            [Cell(CellState.DEAD), Cell(CellState.ALIVE), Cell(CellState.DEAD)] + [Cell(CellState.DEAD) for _ in range(3)],
            [Cell(CellState.DEAD) for _ in range(6)],
            [Cell(CellState.DEAD) for _ in range(6)],
            [Cell(CellState.DEAD) for _ in range(6)]
        ]
        if self.print_debug:
            print("Initial grid")
            self.game_grid.print_grid()
        self.game_grid.update_next_generation()
        if self.print_debug:
            print("Updated grid")
            self.game_grid.print_grid()
        self.excepted_game_grid.grid = [
            [Cell(CellState.ALIVE), Cell(CellState.ALIVE), Cell(CellState.ALIVE)] + [Cell(CellState.DEAD) for _ in range(3)],
            [Cell(CellState.ALIVE), Cell(CellState.DEAD), Cell(CellState.ALIVE)] + [Cell(CellState.DEAD) for _ in range(3)],
            [Cell(CellState.ALIVE), Cell(CellState.ALIVE), Cell(CellState.ALIVE)] + [Cell(CellState.DEAD) for _ in range(3)],
            [Cell(CellState.DEAD) for _ in range(6)],
            [Cell(CellState.DEAD) for _ in range(6)],
            [Cell(CellState.DEAD) for _ in range(6)]
        ]
        if self.print_debug:
            print("Excepted grid")
            self.excepted_game_grid.print_grid()
        self.assertEqual(self.game_grid.grid, self.excepted_game_grid.grid)

    def test_reproduction(self):
        # An empty space with exactly 3 live neighbors should create a new cell
        self.game_grid.grid = [
            [Cell(CellState.DEAD) for _ in range(6)],
            [Cell(CellState.DEAD), Cell(CellState.ALIVE), Cell(CellState.DEAD), Cell(CellState.ALIVE)] + [Cell(CellState.DEAD) for _ in range(2)],
            [Cell(CellState.DEAD), Cell(CellState.DEAD), Cell(CellState.ALIVE)] + [Cell(CellState.DEAD) for _ in range(3)],
            [Cell(CellState.DEAD) for _ in range(6)],
            [Cell(CellState.DEAD) for _ in range(6)],
            [Cell(CellState.DEAD) for _ in range(6)]
        ]
        if self.print_debug:
            print("Initial grid")
            self.game_grid.print_grid()
        self.game_grid.update_next_generation()
        if self.print_debug:
            print("Updated grid")
            self.game_grid.print_grid()
        self.excepted_game_grid.grid = [
            [Cell(CellState.DEAD) for _ in range(6)],
            [Cell(CellState.DEAD), Cell(CellState.DEAD), Cell(CellState.ALIVE)] + [Cell(CellState.DEAD) for _ in range(3)],
            [Cell(CellState.DEAD), Cell(CellState.DEAD), Cell(CellState.ALIVE)] + [Cell(CellState.DEAD) for _ in range(3)],
            [Cell(CellState.DEAD) for _ in range(6)],
            [Cell(CellState.DEAD) for _ in range(6)],
            [Cell(CellState.DEAD) for _ in range(6)]
        ]
        if self.print_debug:
            print("Excepted grid")
            self.excepted_game_grid.print_grid()
        self.assertEqual(self.game_grid.grid, self.excepted_game_grid.grid)




if __name__ == '__main__':
    unittest.main()
