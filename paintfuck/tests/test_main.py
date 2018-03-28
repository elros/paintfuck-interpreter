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
