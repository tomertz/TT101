# Unit Converter: Requirements

## Overview

A command-line unit conversion app written in Python. The user enters a number and a unit code, and the app prints the value converted to the paired unit.

- **Language:** Python 3
- **Executable:** `converter.py`

## Supported units

Each unit converts to exactly one paired unit, in both directions.

| Code | Unit | Converts to | Factor |
|------|------|-------------|--------|
| `lb` | pounds | `kg` | 1 lb = 0.45359237 kg |
| `kg` | kilograms | `lb` | 1 kg = 1 / 0.45359237 lb (about 2.20462) |
| `oz` | US fluid ounces | `ml` | 1 oz = 29.5735295625 ml |
| `ml` | milliliters | `oz` | 1 ml = 1 / 29.5735295625 oz (about 0.033814) |
| `mi` | miles | `km` | 1 mi = 1.609344 km |
| `km` | kilometers | `mi` | 1 km = 1 / 1.609344 mi (about 0.621371) |
| `ft` | feet | `m` | 1 ft = 0.3048 m |
| `m` | meters | `ft` | 1 m = 1 / 0.3048 ft (about 3.28084) |
| `in` | inches | `cm` | 1 in = 2.54 cm |
| `cm` | centimeters | `in` | 1 cm = 1 / 2.54 in (about 0.393701) |

## Input

- Format: `<number> <unit>`, for example `100 mi`.
- The number may be a whole number or a decimal (for example `2.5`).
- The number must be zero or greater. Negative numbers are invalid input.
- The unit code must be one of the codes in the table above.
- Unit codes are not case-sensitive: `100 MI`, `100 Mi`, and `100 mi` are equivalent.
- Leading, trailing, and repeated spaces between the number and the unit are allowed (for example `100   mi`).

## Output

- Format: `<converted value> <target unit>`, for example `160.93 km`.
- The converted value is rounded to 2 decimal places and always shows 2 decimals (for example `254.00 cm`).
- The target unit code is always shown in lowercase.

## Examples

| Input | Output |
|-------|--------|
| `100 mi` | `160.93 km` |
| `150 lb` | `68.04 kg` |
| `10 ft` | `3.05 m` |
| `1 in` | `2.54 cm` |
| `12 oz` | `354.88 ml` |
| `2.5 KG` | `5.51 lb` |

## Program flow

1. Prompt the user for input.
2. If the user types `q` (any case) or presses Enter on an empty line, the app exits.
3. If the input is valid, show the converted result.
4. If the input is invalid, show the error message described below.
5. Show `Press any key to continue...` and keep the result or error on screen until the user presses any key.
6. Return to step 1.

## Invalid input

Input is invalid when any of the following is true:

- It doesn't have exactly two parts: a number and a unit code.
- The number part isn't a valid number.
- The number is negative.
- The unit code isn't in the supported units table.

When input is invalid, the app shows:

```
Invalid input. Use: <number> <unit>, e.g. 100 mi
Valid units: lb, kg, oz, ml, mi, km, ft, m, in, cm
```

The app must not crash on invalid input.

## Platform

- The "press any key" behavior must work on Windows with a single keypress (no Enter required).
- On other operating systems, waiting for Enter is an acceptable fallback.
