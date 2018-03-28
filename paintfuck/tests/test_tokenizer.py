import unittest

from paintfuck.tokenizer import Tokenizer, Command


class TokenizerTestCase(unittest.TestCase):
    def _compare_program_with_tokens(self, program, expected_tokens):
        tokenizer = Tokenizer(program)
        actual_tokens = list(tokenizer)
        self.assertEqual(actual_tokens, expected_tokens)

    def test_tokenizing_simple_program(self):
        self._compare_program_with_tokens(
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

    def test_tokenizing_program_with_excess_chars(self):
        self._compare_program_with_tokens(
            program='A[nXXswew]B',
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

    def test_rolling_back_single_loop(self):
        code = 'we[sn]nw'
        tokenizer = Tokenizer(code)

        tokenizer.skip_forward_to(Command.LOOP_END)
        self.assertEqual(tokenizer.current_position, code.index(']'))

        tokenizer.rollback_loop()
        self.assertEqual(tokenizer.current_position, code.index('[') + 1)

    def test_skipping_single_loop(self):
        code = 'we[sn]nw'
        tokenizer = Tokenizer(code)

        tokenizer.skip_forward_to(Command.LOOP_START)
        self.assertEqual(tokenizer.current_position, code.index('['))

        tokenizer.skip_loop()
        self.assertEqual(tokenizer.current_position, code.index(']') + 1)
