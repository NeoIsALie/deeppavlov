import random
from typing import (
    List,
    Tuple,
    Any
)


class KnightsTour:
    def __init__(self, width: int, height: int):
        """
        Инициализация доски для обхода конем
        :param width: ширина доски
        :param height: длина доски
        """
        self.width: int = width
        self.height: int = height
        self.board: List[Any] = [[None] * self.height for _ in range(self.width)]
        self.knight_tour: List[List[int, int]] = []
        self.moves: List[Tuple[int, int]] = [
            (2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)
        ]

    def _is_valid(self, pos: List[int], passed=False) -> bool:
        """
        Проверка правильности позиции на доске (нахождения в пределах доски)
        :param pos: позиция коня на доске
        :param passed:
        :return:
        """
        if not passed:
            return (
                    0 <= pos[0] < self.width
                    and 0 <= pos[1] < self.height
                    and self.board[pos[0]][pos[1]] is None
            )
        else:
            return (
                    0 <= pos[0] < self.width
                    and 0 <= pos[1] < self.height
            )

    def _possible_moves(self, pos: List[int]) -> List:
        """
        Расчет возможных ходов конем
        :param pos: текущая позиция на доске
        :return: список доступных ходов
        """
        result = []
        moves_num = len(self.moves)
        for move in self.moves:
            new_pos = [pos[0] + move[0], pos[1] + move[1]]
            if self._is_valid(new_pos):
                result.append(new_pos)
        if not result:
            for move in random.sample(self.moves, moves_num):
                new_pos = [pos[0] + move[0], pos[1] + move[1]]
                if self._is_valid(new_pos, passed=True):
                    return [new_pos]
        return result

    def _next_move(self, pos: List[int]) -> List:
        """
        Выбор следующего хода для коня
        :param pos: текущая позиция коня на доске
        :return: следующая позиция на доске
        """
        result = None
        min_weight = 8
        neighbours = self._possible_moves(pos)
        for neighbour in neighbours:
            curr_weight = len(self._possible_moves(neighbour))
            if curr_weight < min_weight:
                result = neighbour
                min_weight = curr_weight
        return result

    def calculate_route(self, start_pos: List[int]) -> None:
        """
        Построение маршрута обхода доски
        :param start_pos: начальная позиция на доске
        :return:
        """
        move_counter = 0
        unique_cells = 0
        curr_pos = start_pos
        area = self.width * self.height

        while unique_cells < area:
            self.knight_tour.append(curr_pos)
            if self.board[curr_pos[0]][curr_pos[1]] is None:
                unique_cells += 1
            self.board[curr_pos[0]][curr_pos[1]] = move_counter
            curr_pos = self._next_move(curr_pos)
            move_counter += 1


def main(desk_size: List) -> List:
    width, height = desk_size
    kt = KnightsTour(width, height)
    kt.calculate_route(start_pos=[0, 0])
    return kt.knight_tour
