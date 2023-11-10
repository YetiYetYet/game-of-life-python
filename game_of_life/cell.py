from __future__ import annotations
from dataclasses import dataclass
from .enums import CellState


@dataclass
class Cell:
    cell_state: CellState = CellState.DEAD

    # def determine_next_state(self, neighbors: list[Cell]) -> CellState:
    #     """determine the next state of the cell based on the state of its neighbors."""
    #     alive_neighbors = 0
    #     for neighbor in neighbors:
    #         if neighbor.cell_state == CellState.ALIVE:
    #             alive_neighbors += 1
    #
    #     if self.cell_state == CellState.ALIVE:
    #         if alive_neighbors < 2:
    #             return CellState.DEAD
    #         elif alive_neighbors > 3:
    #             return CellState.DEAD
    #     elif self.cell_state == CellState.DEAD:
    #         if alive_neighbors == 3:
    #             return CellState.ALIVE


    def set_next_state(self, neighbors: list[Cell]) -> None:
        """set the next state of the cell based on the state of its neighbors."""
        alive_neighbors = 0
        for neighbor in neighbors:
            if neighbor.cell_state == CellState.ALIVE:
                alive_neighbors += 1

        if self.cell_state == CellState.ALIVE:
            if alive_neighbors < 2:
                self.cell_state = CellState.DEAD
            elif alive_neighbors > 3:
                self.cell_state = CellState.DEAD
        elif self.cell_state == CellState.DEAD:
            if alive_neighbors == 3:
                self.cell_state = CellState.ALIVE

