from .tokenizer import Tokenizer, Command


class Interpreter:
    def __init__(self):
        self._tokenizer = None

    def __call__(self, code: str, iterations: int, width: int, height: int):
        self._tokenizer = Tokenizer(code)
