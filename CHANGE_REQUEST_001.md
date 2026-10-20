# Change Request 001: Show Available Conversions at Startup

| Field | Value |
|-------|-------|
| **Change request** | CR-001 |
| **Date** | October 20, 2026 |
| **Requested by** | tomertz |
| **Applies to** | [REQUIREMENTS.md](REQUIREMENTS.md) |
| **Status** | Implemented |
| **Approved** | October 20, 2026, by tomertz |

## Summary

When the program starts, it shows the list of available conversions and short usage instructions. The list is shown once, before the first prompt.

## Reason for the change

Today the app starts with only an input prompt, so a new user doesn't know which units are supported until they enter invalid input and see the error message.

## Current behavior

The program starts and immediately shows:

```
Enter a value and unit (q to quit):
```

## New behavior

The program starts by showing the following text exactly once, followed by a blank line and the input prompt:

```
Unit Converter - available conversions:
  lb (pounds)           <->  kg (kilograms)
  oz (US fluid ounces)  <->  ml (milliliters)
  mi (miles)            <->  km (kilometers)
  ft (feet)             <->  m  (meters)
  in (inches)           <->  cm (centimeters)

Enter a number and a unit, e.g. 100 mi. Type q to quit.

Enter a value and unit:
```

- Each line shows one pair of units, which convert to each other in both directions.
- The list isn't shown again after a conversion or after an error. After the user presses a key to continue, only the input prompt appears.
- Because the instructions now explain how to quit, the input prompt is shortened from `Enter a value and unit (q to quit):` to `Enter a value and unit:`.

## Changes to REQUIREMENTS.md

### "Program flow" section

Add a new first step and renumber the rest. Step 1 of the current flow becomes step 2, and "Return to step 1" becomes "Return to step 2":

1. Show the list of available conversions and the usage instructions, as described in "Startup screen". This step runs only once, when the program starts.
2. Prompt the user for input with `Enter a value and unit:`.
3. If the user types `q` (any case) or presses Enter on an empty line, the app exits.
4. If the input is valid, show the converted result.
5. If the input is invalid, show the error message described below.
6. Show `Press any key to continue...` and keep the result or error on screen until the user presses any key.
7. Return to step 2.

### New "Startup screen" section

Add a new section after "Examples" that contains the startup text shown under "New behavior" above.

## What doesn't change

- The supported units and conversion factors.
- The input rules, including rejecting negative numbers.
- The output format and rounding.
- The invalid-input error message, which still lists the valid units.
- The "Press any key to continue..." behavior.
- How to quit: typing `q` or pressing Enter on an empty line. The instructions only mention `q`, but an empty line still quits.

## Affected files

| File | Change |
|------|--------|
| `REQUIREMENTS.md` | Update as described in "Changes to REQUIREMENTS.md". |
| `converter.py` | Show the startup screen once, and use the shorter input prompt. |
| `test_converter.py` | Add tests for the startup screen. |
| `README.md` | Update the example session to show the startup screen and the new prompt. |

## Acceptance criteria

- The startup screen appears exactly once, when the program starts, and matches the text above.
- Every supported unit code appears on the startup screen.
- After a conversion or an error, pressing a key returns to the input prompt without showing the list again.
- The input prompt reads `Enter a value and unit:`.
- All existing tests still pass.
