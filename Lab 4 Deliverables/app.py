"""
John Leckie, SDEV300, September 11, 2023

PyNumpy Matrix Calculator

This program allows users to enter and validate their phone number and ZIP code. It also enables
users to input values for two 3x3 matrices and perform various matrix operations, including
addition, subtraction, matrix multiplication, and element-wise multiplication. The program utilizes
NumPy for matrix operations and Pandas for displaying results in a user-friendly format.

"""

import re
import numpy as np
import pandas as pd


def validate_phone_number(hopeful_phone):
    """
    Validates a phone number using a regular expression.

    Args:
        hopeful_phone (str): The phone number to validate.

    Returns:
        bool: True if the phone number is valid, False otherwise.
    """
    pattern = r"^\d{3}-\d{3}-\d{4}$"
    return bool(re.match(pattern, hopeful_phone))


def validate_zipcode(hopeful_zip):
    """
    Validates a ZIP code with +4 using a regular expression.

    Args:
        hopeful_zip (str): The ZIP code to validate.

    Returns:
        bool: True if the ZIP code is valid, False otherwise.
    """
    pattern = r"^\d{5}-\d{4}$"
    return bool(re.match(pattern, hopeful_zip))


def get_matrix():
    """
    Gets a 3x3 matrix input from the user.

    Returns:
        numpy.ndarray: A 3x3 matrix created from user input.
    """
    matrix = []
    for i in range(3):
        while True:
            try:
                row = input(f"Enter values for row {i + 1} (space-separated): ").split()
                if len(row) != 3:
                    raise ValueError("Please enter exactly 3 values.")
                row = [float(val) for val in row]
                matrix.append(row)
                break
            except ValueError as err:
                print(f"Invalid input. {err}")

    return np.array(matrix)


# Main loop
print("\n****** PylintedPyNumpyPandas (P^3) Matrix Calculator! ******")
while True:
    play_PyNumpyPandas = input("\nDo you want to run some matrices? (Y/N): ")
    if play_PyNumpyPandas.lower() == "n":
        break
    if play_PyNumpyPandas.lower() != "y":
        print("Please enter 'Y' for Yes or 'N' for No.\n")
        continue

    # Get and validate phone number
    while True:
        phone_number = input("Enter your phone number (XXX-XXX-XXXX): ")
        if validate_phone_number(phone_number):
            break
        print("Please use the XXX-XXX-XXXX numbers-only format.\n")

    # Get and validate ZIP code
    while True:
        zipcode = input("Enter your ZIP code+4 (XXXXX-XXXX): ")
        if validate_zipcode(zipcode):
            break
        print("Please use numbers-only ZIP XXXXX-XXXX format.\n")

    # Get two matrices
    print("\nFor matrix entry, use three space-separated numbers per row. Hit enter after each "
          "row.")
    print("\nEnter your first 3x3 matrix:")
    matrix_a = get_matrix()
    print("\nEnter your second 3x3 matrix:")
    matrix_b = get_matrix()

    # Perform matrix operations
    while True:
        print("\nMatrices are entered!\nSelect a Matrix Operation from the list below:")
        print("a. Addition")
        print("b. Subtraction")
        print("c. Matrix Multiplication")
        print("d. Element by element multiplication")
        print("e. Exit")
        choice = input("Enter your choice: ").lower()

        if choice == "a":
            result = matrix_a + matrix_b
            OPERATION = "Addition"
        elif choice == "b":
            result = matrix_a - matrix_b
            OPERATION = "Subtraction"
        elif choice == "c":
            result = np.matmul(matrix_a, matrix_b)
            OPERATION = "Matrix Multiplication"
        elif choice == "d":
            result = np.multiply(matrix_a, matrix_b)
            OPERATION = "Element by element multiplication"
        elif choice == "e":
            break
        else:
            print("Please select a valid option from the menu.")
            continue

        # Display results using Pandas DataFrame for better formatting
        result_df = pd.DataFrame(result)
        print(f"\nYou selected {OPERATION}. The results are:")
        print(result_df)
        print("\nThe Transpose is:")
        print(result_df.transpose())
        print("\nThe row and column mean values of the results are:")
        print(f"Row: \n{result_df.mean(axis=1).to_string(index=False)}")
        print(f"Column: \n{result_df.mean(axis=0).to_frame().T.to_string(index=False)}")

print("***** Thanks for Using PylintedPyNumpyPandas! *****")
