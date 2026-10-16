LB_TO_KG = 0.45359237


def pounds_to_kg(pounds: float) -> float:
    return pounds * LB_TO_KG


def wait_for_key() -> None:
    print("\nPress any key to exit...")
    try:
        import msvcrt
        msvcrt.getch()
    except ImportError:
        input()


if __name__ == "__main__":
    try:
        pounds = float(input("Enter weight in pounds: "))
        print(f"{pounds} lb = {pounds_to_kg(pounds):.2f} kg")
    except ValueError:
        print("Please enter a valid number.")
    wait_for_key()
