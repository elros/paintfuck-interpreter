import unittest

from paintfuck.tokenizer import Tokenizer, Command


class TokenizerTestCase(unittest.TestCase):
    def compare_program_with_tokens(self, program, expected_tokens):
        tokenizer = Tokenizer(program)
        actual_tokens = list(tokenizer)
        self.assertEqual(actual_tokens, expected_tokens)

    def test_simple_program(self):
        self.compare_program_with_tokens(
            program='nnee[w]',
            expected_tokens=[
                Command.MOVE_NORTH,
                Command.MOVE_NORTH,
                Command.MOVE_EAST,
                Command.MOVE_EAST,
                Command.LOOP_START,
                Command.MOVE_WEST,
                Command.LOOP_END
            ]
        )

    def test_program_with_excess_chars(self):
        self.compare_program_with_tokens(
            program='[nswew]',
            expected_tokens=[
                Command.LOOP_START,
                Command.MOVE_NORTH,
                Command.MOVE_SOUTH,
                Command.MOVE_WEST,
                Command.MOVE_EAST,
                Command.MOVE_WEST,
                Command.LOOP_END
            ]
        )
