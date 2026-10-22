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
| `c` (degrees Celsius) | `f` (degrees Fahrenheit) |
| `f` (degrees Fahrenheit) | `c` (degrees Celsius) |

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
  c  (Celsius)          <->  f  (Fahrenheit)

Enter a number and a unit, e.g. 100 mi. Type q to quit.
```

Enter a number, a space, and a unit code. The result is shown until you press any key, and then you can enter another value:

```
Enter a value and unit: 100 mi
160.93 km
Press any key to continue...
```

Unit codes aren't case-sensitive. Temperatures can be negative, down to absolute zero (−273.15 °C or −459.67 °F). Negative values for any other unit, and unknown units, show an error message with the list of valid units.

To quit, type `q` or press Enter on an empty line.

## Web version

The converter is also available as a web page at **https://tomertz.github.io/TT101/converter/**. It works in any modern browser, including on phones. The first visit takes a few seconds while the browser downloads Python.

To try the web page on your own computer, run this from the project folder:

```powershell
py -m http.server
```

Then open http://localhost:8000/converter/ in a browser.

Some company networks block a file the page needs to load Python, so the page stays on "Loading converter...". If that happens, try a different network.

## Running the tests

```powershell
py -m unittest
```

## More details

See [REQUIREMENTS.md](REQUIREMENTS.md) for the full requirements, including conversion factors and input rules.
