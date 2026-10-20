import math

LB_TO_KG = 0.45359237
OZ_TO_ML = 29.5735295625
MI_TO_KM = 1.609344
FT_TO_M = 0.3048
IN_TO_CM = 2.54

CONVERSIONS = {
    "lb": ("kg", LB_TO_KG),
    "kg": ("lb", 1 / LB_TO_KG),
    "oz": ("ml", OZ_TO_ML),
    "ml": ("oz", 1 / OZ_TO_ML),
    "mi": ("km", MI_TO_KM),
    "km": ("mi", 1 / MI_TO_KM),
    "ft": ("m", FT_TO_M),
    "m": ("ft", 1 / FT_TO_M),
    "in": ("cm", IN_TO_CM),
    "cm": ("in", 1 / IN_TO_CM),
}

ERROR_MESSAGE = (
    "Invalid input. Use: <number> <unit>, e.g. 100 mi\n"
    "Valid units: " + ", ".join(CONVERSIONS)
)


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
    if not math.isfinite(value) or value < 0:
        return None

    target_unit, factor = CONVERSIONS[unit]
    # Adding 0.0 turns -0.0 into 0.0 so "-0" doesn't print as "-0.00".
    result = value * factor + 0.0
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
    while True:
        try:
            text = input("Enter a value and unit (q to quit): ").strip()
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
