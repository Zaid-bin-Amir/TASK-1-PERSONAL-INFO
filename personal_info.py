"""Personal Information Program (Improved)
Accepts a user's basic information and displays it as a clean,
formatted profile.

Concepts practiced: variables, input(), type conversion, f-strings,
functions, loops, and error handling (try/except).
"""

from datetime import date

WIDTH = 40


def get_text(prompt):
    """Keep asking until the user types something non-empty."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  -> This field cannot be empty. Please try again.")


def get_int(prompt, min_value, max_value):
    """Keep asking until the user enters a whole number in range."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("  -> Please enter a whole number (e.g. 21).")
            continue
        if min_value <= value <= max_value:
            return value
        print(f"  -> Please enter a number between {min_value} and {max_value}.")


def get_float(prompt, min_value, max_value):
    """Keep asking until the user enters a number in range."""
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("  -> Please enter a number (e.g. 170.5).")
            continue
        if min_value <= value <= max_value:
            return value
        print(f"  -> Please enter a number between {min_value} and {max_value}.")


def main():
    print("=" * WIDTH)
    print("   PERSONAL INFORMATION PROGRAM")
    print("=" * WIDTH)

    # --- Collect input (input() always returns a string) ---
    full_name = get_text("Full name: ").title()
    age = get_int("Age: ", 1, 120)                        # str -> int
    height_cm = get_float("Height (cm): ", 50, 260)       # str -> float
    city = get_text("City: ").title()
    field_of_study = get_text("Field of study: ").title()
    hobby = get_text("Favorite hobby: ").capitalize()

    # --- Derived values (only possible because of type conversion) ---
    current_year = date.today().year
    birth_year_estimate = current_year - age
    height_m = height_cm / 100
    next_age = age + 1

    # --- Formatted output using f-strings ---
    print()
    print("=" * WIDTH)
    print("           YOUR PROFILE")
    print("=" * WIDTH)
    print(f"{'Name':<18}: {full_name}")
    print(f"{'Age':<18}: {age} years")
    print(f"{'Height':<18}: {height_cm:.1f} cm ({height_m:.2f} m)")
    print(f"{'City':<18}: {city}")
    print(f"{'Field of Study':<18}: {field_of_study}")
    print(f"{'Favorite Hobby':<18}: {hobby}")
    print("-" * WIDTH)
    print(f"Born around {birth_year_estimate}. You'll turn {next_age} next!")
    print("=" * WIDTH)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nProgram cancelled. Goodbye!")