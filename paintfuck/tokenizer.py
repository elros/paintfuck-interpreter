from enum import Enum
from typing import Optional


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
        self._position = 0

    def __iter__(self):
        return self

    def __next__(self) -> Command:
        while self.current_token is None and self.in_code_bound:
            self.forward()

        current_token = self.current_token
        self.forward()

        if not self.in_code_bound:
            raise StopIteration

        return current_token

    def rollback_loop(self):
        # TODO
        pass

    def skip_loop(self):
        # TODO
        pass

    @property
    def current_token(self) -> Optional[Command]:
        if not self.in_code_bound:
            return None

        current_char = self._code[self._position]
        if Command.is_valid_token(current_char):
            return Command(current_char)

    @property
    def in_code_bound(self) -> bool:
        return self._position < len(self._code)

    def forward(self):
        self._position += 1

    def backward(self):
        self._position -= 1
