import io
import unittest
from contextlib import redirect_stdout
from unittest import mock

import converter
from converter import CONVERSIONS, STARTUP_SCREEN, convert


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


class StartupScreenTest(unittest.TestCase):
    def run_main(self, inputs):
        """Run the program with the given inputs and return the prompts and output."""
        prompts = []

        def fake_input(prompt):
            prompts.append(prompt)
            return inputs.pop(0)

        output = io.StringIO()
        with mock.patch("builtins.input", fake_input), \
                mock.patch.object(converter, "wait_for_key"), \
                redirect_stdout(output):
            converter.main()
        return prompts, output.getvalue()

    def test_every_unit_is_listed(self):
        for unit in CONVERSIONS:
            with self.subTest(unit=unit):
                self.assertRegex(STARTUP_SCREEN, rf"\b{unit} +\(")

    def test_shown_once_before_first_prompt(self):
        prompts, output = self.run_main(["100 mi", "abc", "q"])
        self.assertTrue(output.startswith(STARTUP_SCREEN + "\n"))
        self.assertEqual(output.count("available conversions"), 1)
        self.assertEqual(prompts, ["Enter a value and unit: "] * 3)


if __name__ == "__main__":
    unittest.main()
