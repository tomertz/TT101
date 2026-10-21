import math

LB_TO_KG = 0.45359237
OZ_TO_ML = 29.5735295625
MI_TO_KM = 1.609344
FT_TO_M = 0.3048
IN_TO_CM = 2.54
ABSOLUTE_ZERO_C = -273.15
ABSOLUTE_ZERO_F = -459.67


def scale(factor: float):
    return lambda value: value * factor


# unit: (target unit, conversion function, lowest allowed input)
CONVERSIONS = {
    "lb": ("kg", scale(LB_TO_KG), 0.0),
    "kg": ("lb", scale(1 / LB_TO_KG), 0.0),
    "oz": ("ml", scale(OZ_TO_ML), 0.0),
    "ml": ("oz", scale(1 / OZ_TO_ML), 0.0),
    "mi": ("km", scale(MI_TO_KM), 0.0),
    "km": ("mi", scale(1 / MI_TO_KM), 0.0),
    "ft": ("m", scale(FT_TO_M), 0.0),
    "m": ("ft", scale(1 / FT_TO_M), 0.0),
    "in": ("cm", scale(IN_TO_CM), 0.0),
    "cm": ("in", scale(1 / IN_TO_CM), 0.0),
    "c": ("f", lambda c: c * 9 / 5 + 32, ABSOLUTE_ZERO_C),
    "f": ("c", lambda f: (f - 32) * 5 / 9, ABSOLUTE_ZERO_F),
}

ERROR_MESSAGE = (
    "Invalid input. Use: <number> <unit>, e.g. 100 mi\n"
    "Valid units: " + ", ".join(CONVERSIONS)
)

STARTUP_SCREEN = """\
Unit Converter - available conversions:
  lb (pounds)           <->  kg (kilograms)
  oz (US fluid ounces)  <->  ml (milliliters)
  mi (miles)            <->  km (kilometers)
  ft (feet)             <->  m  (meters)
  in (inches)           <->  cm (centimeters)
  c  (Celsius)          <->  f  (Fahrenheit)

Enter a number and a unit, e.g. 100 mi. Type q to quit.
"""


def convert(text: str) -> str | None:
    """Return the converted result, or None if the input is invalid."""
    parts = text.split()
    if len(parts) != 2:
        return None

    number_text, unit = parts[0], parts[1].lower()
    if unit not in CONVERSIONS:
        return None

    try:
        value = float(number_text)
    except ValueError:
        return None
    target_unit, convert_value, minimum = CONVERSIONS[unit]
    if not math.isfinite(value) or value < minimum:
        return None

    # Adding 0.0 turns -0.0 into 0.0 so results that round to zero don't print as "-0.00".
    result = round(convert_value(value), 2) + 0.0
    return f"{result:.2f} {target_unit}"


def wait_for_key() -> None:
    print("Press any key to continue...")
    try:
        import msvcrt
    except ImportError:
        input()
        return
    key = msvcrt.getch()
    # Arrow and function keys send a two-byte sequence; read the second byte too.
    if key in (b"\x00", b"\xe0"):
        msvcrt.getch()


def main() -> None:
    print(STARTUP_SCREEN)
    while True:
        try:
            text = input("Enter a value and unit: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return

        if text == "" or text.lower() == "q":
            return

        result = convert(text)
        print(result if result is not None else ERROR_MESSAGE)
        wait_for_key()
        print()


if __name__ == "__main__":
    main()
