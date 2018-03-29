import unittest

from pntfck.utils import cycle_capped, bitfield_to_str


class UtilitiesTestCase(unittest.TestCase):
    def test_cycle_capped_within_range(self):
        self.assertEqual(8, cycle_capped(8, 0, 10))
        self.assertEqual(5, cycle_capped(5, 0, 100))

    def test_cycle_capped_below_minimum(self):
        self.assertEqual(9, cycle_capped(-1, 0, 10))
        self.assertEqual(99, cycle_capped(-1, 0, 100))

    def test_cycle_capped_above_maximum(self):
        self.assertEqual(0, cycle_capped(99, 0, 10))
        self.assertEqual(0, cycle_capped(999, 0, 100))

    def test_cycle_capped_on_low_border(self):
        self.assertEqual(0, cycle_capped(0, 0, 10))
        self.assertEqual(0, cycle_capped(0, 0, 100))

    def test_cycle_capped_on_top_border(self):
        self.assertEqual(9, cycle_capped(9, 0, 10))
        self.assertEqual(0, cycle_capped(10, 0, 10))
        self.assertEqual(99, cycle_capped(99, 0, 100))
        self.assertEqual(0, cycle_capped(100, 0, 100))

    def test_bitfield_to_str(self):
        self.assertEqual('00\r\n00', bitfield_to_str(
            [
                [0, 0],
                [0, 0],
            ]
        ))
        self.assertEqual('010\r\n101\r\n111', bitfield_to_str(
            [
                [0, 1, 0],
                [1, 0, 1],
                [1, 1, 1],
            ]
        ))
        self.assertEqual('111\r\n000\r\n001', bitfield_to_str(
            [
                [True, True, True],
                [False, False, False],
                [False, False, True],
            ]
        ))
