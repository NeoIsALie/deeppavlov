import random
from typing import (
    List,
    Any
)


class KnightsTour:
    def __init__(self, width, height):
        self.width: int = width
        self.height: int = height
        self.board: List[Any] = [[None] * self.height for _ in range(self.width)]
        self.knight_tour: List[List[int, int]] = []

    def __is_valid(self, pos: List[int], passed=False) -> bool:
        if not passed:
            return (
                    0 <= pos[0] < self.width
                    and 0 <= pos[1] < self.height
                    and self.board[pos[0]][pos[1]] is None
            )
        else:
            return 0 <= pos[0] < self.width and 0 <= pos[1] < self.height

    def __possible_moves(self, pos: List[int]) -> List:
        result = []
        moves = [(2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]
        for move in moves:
            new_pos = [pos[0] + move[0], pos[1] + move[1]]
            if self.__is_valid(new_pos):
                result.append(new_pos)
        if not result:
            for move in random.sample(moves, len(moves)):
                new_pos = [pos[0] + move[0], pos[1] + move[1]]
                if self.__is_valid(new_pos, passed=True):
                    return [new_pos]
        return result

    def __next_move(self, pos: List[int]) -> List:
        result = None
        min_weight = 8  # the max number of options for the knight's next move
        neighbours = self.__possible_moves(pos)
        for neighbour in neighbours:
            curr_weight = len(self.__possible_moves(neighbour))
            if curr_weight < min_weight:
                result = neighbour
                min_weight = curr_weight
        return result

    def calculate_route(self, start_pos: List[int]) -> None:
        move_counter = 0
        unique_cells = 0
        curr_pos = start_pos
        area = self.width * self.height

        while unique_cells < area:
            self.knight_tour.append(curr_pos)
            if self.board[curr_pos[0]][curr_pos[1]] is None:
                unique_cells += 1
            self.board[curr_pos[0]][curr_pos[1]] = move_counter
            curr_pos = self.__next_move(curr_pos)
            move_counter += 1


def main(desk_size: List) -> List:
    width, height = desk_size
    kt = KnightsTour(width, height)
    kt.calculate_route(start_pos=[0, 0])
    return kt.knight_tour
