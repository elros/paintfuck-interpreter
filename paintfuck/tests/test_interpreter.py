import unittest

from paintfuck.interpreter import Interpreter


class InterpreterTestCase(unittest.TestCase):
    def _compare_program_with_output(self, program, iterations, width, height, expected_output):
        interpreter = Interpreter(width, height)
        actual_output = interpreter.run_program(program, iterations)
        self.assertEqual(expected_output, actual_output)

    def test_interpreting_simple_program(self):
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

    def test_interpreting_simple_program_with_excess_iterations(self):
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

    def test_interpreting_simple_program_with_insufficient_iterations(self):
        self._compare_program_with_output(
            program='*s*',
            iterations=2,
            width=3,
            height=3,
            expected_output=[
                [1, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ]
        )

    def test_interpreting_simple_program_with_non_command_chars(self):
        self._compare_program_with_output(
            program='X*Ys*Z',
            iterations=6,
            width=3,
            height=3,
            expected_output=[
                [1, 0, 0],
                [1, 0, 0],
                [0, 0, 0]
            ]
        )

    def test_interpreting_simple_loops(self):
        self._compare_program_with_output(
            program='*[s]*',
            iterations=10,
            width=3,
            height=3,
            expected_output=[
                [1, 0, 0],
                [1, 0, 0],
                [0, 0, 0]
            ]
        )
        self._compare_program_with_output(
            program='[s]e*',
            iterations=10,
            width=3,
            height=3,
            expected_output=[
                [0, 1, 0],
                [0, 0, 0],
                [0, 0, 0]
            ]
        )

    def test_interpreting_embedded_loops(self):
        self._compare_program_with_output(
            program='[[*]]',
            iterations=100,
            width=3,
            height=3,
            expected_output=[
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ]
        )

    def test_interpreting_loop_rollback(self):
        self._compare_program_with_output(
            program='*[s*]',
            iterations=5,
            width=3,
            height=3,
            expected_output=[
                [1, 0, 0],
                [1, 0, 0],
                [0, 0, 0]
            ]
        )

    def test_interpreting_with_iterations_limit(self):
        self._compare_program_with_output(
            program='*s*s*',
            iterations=0,
            width=3,
            height=3,
            expected_output=[
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ]
        )
        self._compare_program_with_output(
            program='*s*s*',
            iterations=3,
            width=3,
            height=3,
            expected_output=[
                [1, 0, 0],
                [1, 0, 0],
                [0, 0, 0]
            ]
        )

    def test_interpretting_with_single_border_crossing(self):
        self._compare_program_with_output(
            program='*n*',
            iterations=100,
            width=3,
            height=3,
            expected_output=[
                [1, 0, 0],
                [0, 0, 0],
                [1, 0, 0]
            ]
        )
        self._compare_program_with_output(
            program='*w*',
            iterations=100,
            width=3,
            height=3,
            expected_output=[
                [1, 0, 1],
                [0, 0, 0],
                [0, 0, 0]
            ]
        )

    def test_interpretting_with_multiple_border_crossings(self):
        self._compare_program_with_output(
            program='*w*n*',
            iterations=100,
            width=3,
            height=3,
            expected_output=[
                [1, 0, 1],
                [0, 0, 0],
                [0, 0, 1]
            ]
        )
