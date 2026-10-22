from pyscript import document, when

from converter import STARTUP_SCREEN, convert

INVALID_MESSAGE = (
    "Invalid value. Only temperatures (c, f) can be negative, "
    "and not below absolute zero."
)

number_box = document.getElementById("number")
unit_box = document.getElementById("unit")
result = document.getElementById("result")


def show(text: str, css_class: str = "") -> None:
    result.textContent = text
    result.className = css_class


@when("input", "#number, #unit")
def update(event) -> None:
    text = number_box.value.strip()
    if text == "":
        show("")
        return

    converted = convert(f"{text} {unit_box.value}")
    if converted is None:
        show(INVALID_MESSAGE, "message invalid")
    else:
        show(converted)


conversion_lines = [line for line in STARTUP_SCREEN.splitlines() if line.startswith("  ")]
document.getElementById("conversions").textContent = "\n".join(conversion_lines)

show("")
number_box.disabled = False
unit_box.disabled = False
