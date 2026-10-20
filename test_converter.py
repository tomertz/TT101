import unittest

from converter import convert


class RequirementsExamplesTest(unittest.TestCase):
    def test_examples(self):
        examples = {
            "100 mi": "160.93 km",
            "150 lb": "68.04 kg",
            "10 ft": "3.05 m",
            "1 in": "2.54 cm",
            "12 oz": "354.88 ml",
            "2.5 KG": "5.51 lb",
        }
        for text, expected in examples.items():
            with self.subTest(text=text):
                self.assertEqual(convert(text), expected)


class ConversionTest(unittest.TestCase):
    def test_every_unit(self):
        cases = {
            "1 lb": "0.45 kg",
            "1 kg": "2.20 lb",
            "1 oz": "29.57 ml",
            "100 ml": "3.38 oz",
            "1 mi": "1.61 km",
            "100 km": "62.14 mi",
            "100 ft": "30.48 m",
            "1 m": "3.28 ft",
            "100 in": "254.00 cm",
            "254 cm": "100.00 in",
        }
        for text, expected in cases.items():
            with self.subTest(text=text):
                self.assertEqual(convert(text), expected)

    def test_unit_case_is_ignored(self):
        for text in ("100 mi", "100 MI", "100 Mi", "100 mI"):
            with self.subTest(text=text):
                self.assertEqual(convert(text), "160.93 km")

    def test_extra_spaces_are_allowed(self):
        self.assertEqual(convert("  100   mi  "), "160.93 km")

    def test_zero(self):
        self.assertEqual(convert("0 lb"), "0.00 kg")
        self.assertEqual(convert("-0 lb"), "0.00 kg")


class InvalidInputTest(unittest.TestCase):
    def test_invalid_input_returns_none(self):
        cases = [
            "-5 ft",
            "-0.01 kg",
            "100",
            "mi",
            "100 yd",
            "abc mi",
            "mi 100",
            "100 mi extra",
            "nan mi",
            "inf km",
            "",
        ]
        for text in cases:
            with self.subTest(text=text):
                self.assertIsNone(convert(text))


if __name__ == "__main__":
    unittest.main()
