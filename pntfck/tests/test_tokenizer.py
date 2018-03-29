import unittest

from pntfck.tokenizer import Tokenizer, Command


class TokenizerTestCase(unittest.TestCase):
    def _compare_program_with_tokens(self, program, expected_tokens):
        tokenizer = Tokenizer(program)
        actual_tokens = list(tokenizer)
        self.assertEqual(expected_tokens, actual_tokens)

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
        self.assertEqual(code.index(']'), tokenizer.current_position)

        tokenizer.rollback_loop()
        self.assertEqual(code.index('['), tokenizer.current_position)

    def test_skipping_single_loop(self):
        code = 'we[sn]nw'
        tokenizer = Tokenizer(code)

        tokenizer.skip_forward_to(Command.LOOP_START)
        self.assertEqual(code.index('['), tokenizer.current_position)

        tokenizer.skip_loop()
        self.assertEqual(code.index(']'), tokenizer.current_position)
