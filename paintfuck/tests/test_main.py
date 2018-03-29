import unittest

from paintfuck.main import interpreter


class MainModuleTestCase(unittest.TestCase):
    def test_main_module_with_empty_program(self):
        self.assertEqual('00\r\n00', interpreter(
            code='',
            iterations=10,
            width=2,
            height=2
        ))

    def test_main_module_with_simple_program(self):
        self.assertEqual('10\r\n10', interpreter(
            code='*s*',
            iterations=10,
            width=2,
            height=2
        ))

    def test_main_module_with_complex_program(self):
        code = '*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*'
        width = 6
        height = 9

        def partial_run(iterations):
            return interpreter(code, iterations, width, height)

        test_cases = [
            (0, '\r\n'.join(['000000',
                             '000000',
                             '000000',
                             '000000',
                             '000000',
                             '000000',
                             '000000',
                             '000000',
                             '000000'])),
            (7, '\r\n'.join(['111100',
                             '000000',
                             '000000',
                             '000000',
                             '000000',
                             '000000',
                             '000000',
                             '000000',
                             '000000'])),
            (19, '\r\n'.join(['111100',
                              '000010',
                              '000001',
                              '000010',
                              '000100',
                              '000000',
                              '000000',
                              '000000',
                              '000000'])),
            (42, '\r\n'.join(['111100',
                              '100010',
                              '100001',
                              '100010',
                              '111100',
                              '100000',
                              '100000',
                              '100000',
                              '100000'])),
            (100, '\r\n'.join(['111100',
                               '100010',
                               '100001',
                               '100010',
                               '111100',
                               '100000',
                               '100000',
                               '100000',
                               '100000'])),
        ]

        for iterations, result in test_cases:
            self.assertEqual(result, partial_run(iterations))
