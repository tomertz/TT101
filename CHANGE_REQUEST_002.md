# Change Request 002: Add Temperature Conversion

| Field | Value |
|-------|-------|
| **Change request** | CR-002 |
| **Date** | October 21, 2026 |
| **Requested by** | tomertz |
| **Applies to** | [REQUIREMENTS.md](REQUIREMENTS.md) |
| **Status** | Implemented |
| **Approved** | October 21, 2026, by tomertz |

## Summary

Add conversion between degrees Celsius (`c`) and degrees Fahrenheit (`f`), in both directions.

## Reason for the change

The app supports weight, volume, and length, but not temperature, which is one of the most common everyday conversions.

## New units

| Code | Unit | Converts to | Formula |
|------|------|-------------|---------|
| `c` | degrees Celsius | `f` | °F = °C × 9/5 + 32 |
| `f` | degrees Fahrenheit | `c` | °C = (°F − 32) × 5/9 |

Unlike the existing units, temperature can't be converted by multiplying by a single factor, because the two scales have different zero points. The formulas above must be used instead.

## Negative values

The current requirements reject all negative numbers. Temperatures are often below zero (for example `-10 c`), so this change makes an exception for temperature:

- **Negative values are allowed for `c` and `f`.**
- **Values below absolute zero are invalid**, because no real temperature can be colder. Absolute zero is −273.15 °C, which equals −459.67 °F. For example, `-273.15 c` is valid but `-300 c` is invalid.
- **Negative values are still invalid for every other unit**, as today.

## Output

- Results use the same format and rounding as other units, for example `212.00 f`.
- Results can now be negative, for example `-23.33 c`.
- A result that rounds to zero shows as `0.00`, never `-0.00`.

## Examples

| Input | Output | Notes |
|-------|--------|-------|
| `100 c` | `212.00 f` | Water boils |
| `0 c` | `32.00 f` | Water freezes |
| `37 C` | `98.60 f` | Body temperature, uppercase unit |
| `32 f` | `0.00 c` | |
| `98.6 f` | `37.00 c` | |
| `-40 c` | `-40.00 f` | The two scales are equal at −40 |
| `-10 f` | `-23.33 c` | Negative input and output |
| `-273.15 c` | `-459.67 f` | Absolute zero, still valid |
| `-300 c` | Invalid input | Below absolute zero |
| `-500 f` | Invalid input | Below absolute zero |
| `-5 kg` | Invalid input | Negative values are still invalid for non-temperature units |

## Changes to REQUIREMENTS.md

### "Supported units" section

- Add the two rows from "New units" above to the table.
- Rename the table's "Factor" column to "Conversion", because the temperature rows use formulas instead of factors.

### "Input" section

Replace the line "The number must be zero or greater. Negative numbers are invalid input." with:

- For `c` and `f`, the number may be negative, but must not be below absolute zero (−273.15 for `c`, −459.67 for `f`).
- For all other units, the number must be zero or greater. Negative numbers are invalid input.

### "Output" section

Add:

- Temperature results can be negative. A result that rounds to zero shows as `0.00`, not `-0.00`.

### "Examples" section

Add these rows: `100 c` → `212.00 f`, `98.6 f` → `37.00 c`, and `-40 c` → `-40.00 f`.

### "Startup screen" section

Add a line for temperature at the end of the conversion list:

```
Unit Converter - available conversions:
  lb (pounds)           <->  kg (kilograms)
  oz (US fluid ounces)  <->  ml (milliliters)
  mi (miles)            <->  km (kilometers)
  ft (feet)             <->  m  (meters)
  in (inches)           <->  cm (centimeters)
  c  (Celsius)          <->  f  (Fahrenheit)

Enter a number and a unit, e.g. 100 mi. Type q to quit.
```

### "Invalid input" section

Replace the line "The number is negative." with:

- The number is negative and the unit isn't `c` or `f`.
- The number is below absolute zero for `c` or `f`.

Update the list of valid units in the error message:

```
Invalid input. Use: <number> <unit>, e.g. 100 mi
Valid units: lb, kg, oz, ml, mi, km, ft, m, in, cm, c, f
```

## What doesn't change

- The existing units, their conversion factors, and their results.
- The input format, case-insensitivity, and handling of extra spaces.
- Rounding to 2 decimal places.
- The program flow, the input prompt, and the "Press any key to continue..." behavior.
- How to quit.

## Affected files

| File | Change |
|------|--------|
| `REQUIREMENTS.md` | Update as described in "Changes to REQUIREMENTS.md". |
| `converter.py` | Add the two temperature units with their formulas, the absolute-zero check, and the new startup screen line. |
| `test_converter.py` | Add tests for every example in this change request. |
| `README.md` | Add the temperature units to the supported units table and the startup screen example. |

## Acceptance criteria

- Every example in the "Examples" table above produces the listed output.
- `c` and `f` appear on the startup screen and in the invalid-input error message.
- Negative values are still rejected for every non-temperature unit.
- No result displays as `-0.00`.
- All existing tests still pass.
