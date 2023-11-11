from __future__ import annotations
from dataclasses import dataclass
from .enums import CellState

@dataclass
class Cell:
    cell_state: CellState = CellState.DEAD

    @classmethod
    def determine_next_state(cls, actual_cell_state, neighbors: list[Cell]) -> CellState:
        """determine the next state of the cell based on the state of its neighbors."""
        alive_neighbors = sum(1 for neighbor in neighbors if neighbor.cell_state == CellState.ALIVE)
        if actual_cell_state == CellState.ALIVE and (alive_neighbors < 2 or alive_neighbors > 3):
            return CellState.DEAD
        elif actual_cell_state == CellState.DEAD and alive_neighbors == 3:
            return CellState.ALIVE

    def set_next_state(self, neighbors: list[Cell]) -> None:
        """Set the next state of the cell based on the state of its neighbors."""
        alive_neighbors = sum(1 for neighbor in neighbors if neighbor.cell_state == CellState.ALIVE)

        if self.cell_state == CellState.ALIVE and (alive_neighbors < 2 or alive_neighbors > 3):
            self.cell_state = CellState.DEAD
        elif self.cell_state == CellState.DEAD and alive_neighbors == 3:
            self.cell_state = CellState.ALIVE

