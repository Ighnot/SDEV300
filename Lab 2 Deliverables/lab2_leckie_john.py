"""
John Leckie, SDEV 300, Lab 2

lab2_leckie_john offers a menu-driven interface to perform various tasks:
- Generate secure passwords based on user-defined length and complexity attributes.
- Calculate percentages from user-entered numerator, denominator, and precision.
- Determine the number of days from now to July 4, 2025.
- Use Law of Cosines to find the length of a triangle's side. User enters two sides and angle.
- Calculate the volume of a right circular cylinder. User enters radius and height.
The user is guided through each function with prompts and error-handling to ensure valid inputs.
"""

import math
import datetime
import random


def generate_secure_password():
    """
    Generates a secure password based on user-defined length and complexity attributes.

    The user is prompted to input the desired length and complexity attributes (uppercase,
    lowercase, numbers, special characters) for the password.  It can be any or all, but
    must be at least one. The function then generates a password that matches the
    specified attributes and length. random module imported.
    """
    length = input("Enter the length of the password: ")

    # Validate input to ensure it's a positive integer
    while not length.isdigit() or int(length) <= 0:
        print("Invalid input. Please enter a positive integer.")
        length = input("Enter the length of the password: ")

    length = int(length)

    while True:
        complexity = input(
            "Enter desired complexity attributes (U: Upper Case, L: Lower Case, N: Numbers, "
            "S: Special characters): ").lower()

        # Gives the function characters to randomly choose from, based on complexity result
        characters = ''
        if 'u' in complexity:
            characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if 'l' in complexity:
            characters += 'abcdefghijklmnopqrstuvwxyz'
        if 'n' in complexity:
            characters += '0123456789'
        if 's' in complexity:
            characters += '!@#$%^&*()'

        if characters:
            break
        print("Please select at least one complexity attribute.")

    secure_password = ''.join(random.choice(characters) for _ in range(length))
    secure_password = secure_password.replace(" ", "")  # Remove spaces from password
    print("Generated Secure Password:", secure_password)


def calculate_and_format_percentage():
    """
    Calculates and formats a percentage based on user inputs.

    The user is prompted to enter the numerator, denominator, and the number of decimal points
    for formatting. The function then calculates the percentage and formats it according to
    the user's specifications.
    """
    numerator = input("Enter the numerator: ")

    while not numerator.isdigit() or int(numerator) < 0:
        print("Invalid input. Please enter a non-negative integer.")
        numerator = input("Enter the numerator: ")

    numerator = float(numerator)

    denominator = input("Enter the denominator: ")

    while not denominator.isdigit() or int(denominator) <= 0:
        print("Invalid input. Please enter a positive integer for the denominator.")
        denominator = input("Enter the denominator: ")

    denominator = float(denominator)

    decimal_points = input("Enter the number of decimal points: ")

    while not decimal_points.isdigit() or int(decimal_points) < 0:
        print("Invalid input. Please enter a non-negative integer for decimal points.")
        decimal_points = input("Enter the number of decimal points: ")

    decimal_points = int(decimal_points)

    percentage = (numerator / denominator) * 100
    formatted_percentage = f"{percentage:.{decimal_points}f}"

    print("Formatted Percentage:", formatted_percentage, "%")


def days_until_july_4_2025():
    """
    Calculates and displays the number of days from the current date until July 4, 2025.

    The function calculates the difference in days between the current date and July 4, 2025,
    and then displays the result to the user. datetime module imported.
    """
    current_date = datetime.datetime.now().date()
    target_date = datetime.date(2025, 7, 4)
    days_remaining = (target_date - current_date).days
    print("Days between now and July 4, 2025:", days_remaining, "days. So, forever, basically.")


def law_of_cosines():
    """
    Calculates the length of a triangle's side using the Law of Cosines.

    The user is prompted to input the lengths of two sides of a triangle and the angle between
    them. The function then calculates and displays the length of the third side using the Law
    of Cosines. math module imported.
    """
    while True:
        try:
            side_a = float(input("Enter the length of side a: "))
            side_b = float(input("Enter the length of side b: "))
            angle_c = float(input("Enter the angle in degrees (angle C): "))

            if 0 < side_a < 90 and 0 < side_b < 90 and 0 < angle_c < 90:
                break
            print("Invalid input. Please ensure side_a and side_b are non-negative and nonzero."
                  " Angle_c must be non-negative and less than 90 degrees.")

        except ValueError:
            print("Invalid input. Use numeric values > 0 for side_a, side_b, and angle_c.")

    angle_c = math.radians(angle_c)

    side_c = math.sqrt(side_a ** 2 + side_b ** 2 - 2 * side_a * side_b * math.cos(angle_c))
    print("Length of side c:", side_c)


def volume_of_right_circular_cylinder():
    """
    Calculates and displays the volume of a right circular cylinder.

    The user is prompted to input the radius and height of the cylinder. The function then
    calculates and displays the volume of the cylinder. math module imported.
    """
    while True:
        try:
            radius = float(input("Enter the radius of the cylinder: "))
            height = float(input("Enter the height of the cylinder: "))

            if radius > 0 and height > 0:
                break
            print("Invalid input. Radius and height must be non-negative and nonzero.")

        except ValueError:
            print("Invalid input. Please enter numeric values for radius and height.")

    volume = math.pi * radius ** 2 * height
    print("Volume of the cylinder:", volume)


def main():
    """
    Main function-- displays the menu and handles user choices.

    This function provides a menu-driven interface for the user to select various options.
    It repeatedly displays the menu, takes the user's choice, and executes the corresponding
    function based on the user's input. The loop continues until the user selects the 'f' option
    to exit the program.
    """
    while True:
        print("\nMenu:")
        print("a. Generate Secure Password")
        print("b. Calculate and Format a Percentage")
        print("c. How many days from today until July 4, 2025?")
        print("d. Use the Law of Cosines to calculate the leg of a triangle.")
        print("e. Calculate the volume of a Right Circular Cylinder")
        print("f. Exit program")

        choice = input("Select an option (a through f): ").lower()

        if choice == 'a':
            generate_secure_password()
        elif choice == 'b':
            calculate_and_format_percentage()
        elif choice == 'c':
            days_until_july_4_2025()
        elif choice == 'd':
            law_of_cosines()
        elif choice == 'e':
            volume_of_right_circular_cylinder()
        elif choice == 'f':
            print("Exiting-- Thank you for helping a poor student become a programmer!")
            break
        else:
            print("Please use a letter from a to f in the English alphabet.")


if __name__ == "__main__":
    main()
