from enum import Enum
from typing import Optional, Callable


class Command(Enum):
    MOVE_NORTH = 'n'
    MOVE_EAST = 'e'
    MOVE_SOUTH = 's'
    MOVE_WEST = 'w'
    FLIP_BIT = '*'
    LOOP_START = '['
    LOOP_END = ']'

    @classmethod
    def is_valid_token(cls, token):
        for command in cls:
            if command.value == token:
                return True
        else:
            return False


class Tokenizer:
    def __init__(self, code: str):
        self._code = code
        self._position = -1  # Start before the first symbol

    def __iter__(self):
        return self

    def __next__(self) -> Command:
        self.step_forward()
        while not self.current_token_is_valid and self.is_within_code_bounds:
            self.step_forward()

        if not self.is_within_code_bounds:
            raise StopIteration

        return self.current_token

    def rollback_loop(self):
        self._looping_helper(
            step_fn=self.step_backward,
            opening_token=Command.LOOP_END,
            closing_token=Command.LOOP_START
        )

    def skip_loop(self):
        self._looping_helper(
            step_fn=self.step_forward,
            opening_token=Command.LOOP_START,
            closing_token=Command.LOOP_END
        )

    @property
    def current_position(self) -> int:
        return self._position

    @property
    def current_token_is_valid(self) -> bool:
        return self.current_token is not None

    @property
    def current_token(self) -> Optional[Command]:
        if not self.is_within_code_bounds:
            return None

        current_char = self._code[self._position]
        if Command.is_valid_token(current_char):
            return Command(current_char)

    @property
    def is_within_code_bounds(self) -> bool:
        return 0 <= self._position < len(self._code)

    def step_forward(self):
        self._position += 1

    def step_backward(self):
        self._position -= 1

    def skip_forward_to(self, token: Command):
        while self.current_token != token:
            self.step_forward()

    def _looping_helper(self, step_fn: Callable, opening_token: Command, closing_token: Command):
        depth = 1  # Because current_token is a loop command

        # Loop until all matching loop tokens found
        while depth != 0:
            step_fn()
            if self.current_token == opening_token:
                depth += 1
            elif self.current_token == closing_token:
                depth -= 1
