import unittest

from day1 import calibration_value, calibration_value_sum


class Test(unittest.TestCase):
    def test_calibration_value(self):
        self.assertEqual(calibration_value("1abc2"), 12)
        self.assertEqual(calibration_value("pqr3stu8vwx"), 38)
        self.assertEqual(calibration_value("a1b2c3d4e5f"), 15)
        self.assertEqual(calibration_value("treb7uchet"), 77)

    def test_calibration_value_parse(self):
        self.assertEqual(calibration_value("two1nine", True), 29)
        self.assertEqual(calibration_value("eightwothree", True), 83)
        self.assertEqual(calibration_value("abcone2threexyz", True), 13)
        self.assertEqual(calibration_value("xtwone3four", True), 24)
        self.assertEqual(calibration_value("4nineeightseven2", True), 42)
        self.assertEqual(calibration_value("zoneight234", True), 14)
        self.assertEqual(calibration_value("7pqrstsixteen", True), 76)

    def test_calibration_value_sum(self):
        self.assertEqual(
            calibration_value_sum(
                """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
                """.strip().splitlines()
            ),
            142,
        )

    def test_calibration_value_sum_parse(self):
        self.assertEqual(
            calibration_value_sum(
                """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
                """.strip().splitlines(),
                True,
            ),
            281,
        )
