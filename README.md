# Unit Converter

A command-line app that converts a value between common imperial and metric units.

## Supported units

| Enter | Converts to |
|-------|-------------|
| `lb` (pounds) | `kg` (kilograms) |
| `kg` (kilograms) | `lb` (pounds) |
| `oz` (US fluid ounces) | `ml` (milliliters) |
| `ml` (milliliters) | `oz` (US fluid ounces) |
| `mi` (miles) | `km` (kilometers) |
| `km` (kilometers) | `mi` (miles) |
| `ft` (feet) | `m` (meters) |
| `m` (meters) | `ft` (feet) |
| `in` (inches) | `cm` (centimeters) |
| `cm` (centimeters) | `in` (inches) |

## Running the app

Requires Python 3.10 or later. On Windows, run:

```powershell
py converter.py
```

On macOS or Linux, run `python3 converter.py`.

The app starts by listing the available conversions:

```
Unit Converter - available conversions:
  lb (pounds)           <->  kg (kilograms)
  oz (US fluid ounces)  <->  ml (milliliters)
  mi (miles)            <->  km (kilometers)
  ft (feet)             <->  m  (meters)
  in (inches)           <->  cm (centimeters)

Enter a number and a unit, e.g. 100 mi. Type q to quit.
```

Enter a number, a space, and a unit code. The result is shown until you press any key, and then you can enter another value:

```
Enter a value and unit: 100 mi
160.93 km
Press any key to continue...
```

Unit codes aren't case-sensitive. Negative numbers and unknown units show an error message with the list of valid units.

To quit, type `q` or press Enter on an empty line.

## Running the tests

```powershell
py -m unittest
```

## More details

See [REQUIREMENTS.md](REQUIREMENTS.md) for the full requirements, including conversion factors and input rules.
