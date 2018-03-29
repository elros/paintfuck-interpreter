from typing import List

from pntfck.utils import cycle_capped
from .tokenizer import Tokenizer


class Interpreter:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._field = self._build_field(height, width)

        # Start at the top left corner
        self._row = 0
        self._column = 0

        self._tokenizer: Tokenizer = None

    def run_program(self, code: str, iterations: int) -> List[List[int]]:
        self._tokenizer = Tokenizer(code)

        try:
            for _ in range(iterations):
                self._perform_iteration()
        except StopIteration:
            # We're at the end of code with excessive iterations, just skip them
            pass

        return self._field

    @staticmethod
    def _build_field(height, width):
        return [[False for _ in range(width)] for _ in range(height)]

    def _perform_iteration(self):
        token = next(self._tokenizer)
        token_handler_name = '_perform__{action}'.format(action=token.name.lower())
        token_handler = getattr(self, token_handler_name)
        token_handler()

    def _perform__move_north(self):
        self._row = cycle_capped(self._row - 1, low=0, top=self._height)

    def _perform__move_south(self):
        self._row = cycle_capped(self._row + 1, low=0, top=self._height)

    def _perform__move_west(self):
        self._column = cycle_capped(self._column - 1, low=0, top=self._width)

    def _perform__move_east(self):
        self._column = cycle_capped(self._column + 1, low=0, top=self._width)

    def _perform__flip_bit(self):
        self.current_bit = not self.current_bit

    def _perform__loop_start(self):
        if not self.current_bit:
            self._tokenizer.skip_loop()

    def _perform__loop_end(self):
        if self.current_bit:
            self._tokenizer.rollback_loop()

    @property
    def current_bit(self) -> bool:
        return self._field[self._row][self._column]

    @current_bit.setter
    def current_bit(self, value: bool):
        self._field[self._row][self._column] = value
