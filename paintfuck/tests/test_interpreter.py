import unittest

from paintfuck.interpreter import Interpreter


class InterpreterTestCase(unittest.TestCase):
    def _compare_program_with_output(self, program, iterations, width, height, expected_output):
        interpreter = Interpreter(width, height)
        actual_output = interpreter.run_program(program, iterations)
        self.assertEqual(expected_output, actual_output)

    def test_interpreting_simple_command(self):
        self._compare_program_with_output(
            program='*s*',
            iterations=3,
            width=3,
            height=3,
            expected_output=[
                [1, 0, 0],
                [1, 0, 0],
                [0, 0, 0]
            ]
        )

    def test_interpreting_simple_command_with_redundant_iterations(self):
        self._compare_program_with_output(
            program='*s*',
            iterations=100,
            width=3,
            height=3,
            expected_output=[
                [1, 0, 0],
                [1, 0, 0],
                [0, 0, 0]
            ]
        )
