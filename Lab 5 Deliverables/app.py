"""
John Leckie, SDEV300, 16 Sep 2023

This program provides a menu-driven interface for analyzing two datasets (Population Data
and Housing Data) from CSV files. It calculates statistics (count, mean, standard deviation, min,
max) and optionally displays histograms. It uses Pandas for data manipulation and Matplotlib for
visualization.
"""

import sys
import matplotlib.pyplot as plt
import pandas as pd

# Define file paths for the datasets
HOUSING = "Housing.csv"
POP_CHANGE = "PopChange.csv"


def main_menu():
    """
    Display the main menu, allowing the user to choose a dataset for analysis.
    """
    menu_items = {1: "Population Data",
                  2: "Housing Data",
                  3: "Exit"}

    while True:
        for item, description in menu_items.items():
            print(item, "\t", description)  # Display menu options

        try:
            selection = int(input("\nPlease make a numerical selection:\t"))  # Get user input

            if selection == 1:
                read_file(POP_CHANGE)
            elif selection == 2:
                read_file(HOUSING)
            elif selection == 3:
                print("\nExiting program, thank you!")
                sys.exit()  # Exit program
            else:
                print("\nUse one of the specified choices (1, 2, 3).\n")
        except ValueError:
            print("\nUse one of the specified choices (1, 2, 3).\n")


def read_file(file):
    """
    Read a CSV file and pass the data to the corresponding class for analysis.
    :param file: The path to the CSV file.
    """
    data_frame = pd.read_csv(file)  # Read the CSV file

    if file == POP_CHANGE:
        PopChange(data_frame)
    else:
        Housing(data_frame)


def generate_histogram(data, title, x_label):
    """
    Generate a histogram from the data for display to the user.
    :param data: The data to create a histogram from.
    :param title: The title for the histogram.
    :param x_label: The x-axis label, keyed off the column selection within each class.
    """

    plt.hist(data, bins="auto")  # Plot the histogram with selected data

    plt.grid(True)

    plt.title(title)  # Set the title

    plt.xlabel(x_label)  # Set the x-axis label dynamically based on the column
    plt.ylabel("# Data Points")  # Set label to explain y-axis' meaning (mostly to me)

    plt.show()  # Display the histogram (optional)


class PopChange:
    """
    This class represents the analysis of population change data.

    It provides methods to analyze specific columns of the dataset and display statistics
    such as count, mean, standard deviation, min, max, and histograms.
    """
    def __init__(self, data_frame):
        self.data_frame = data_frame

        self.display_menu()  # Display selection menu

    def display_menu(self):
        """
        Display menu to allow user to select a column from the data file for analysis.
        """
        menu_items = {
            1: "Pop Apr 1",
            2: "Pop Jul 1",
            3: "Change Pop",
            4: "Return to Menu",
        }

        while True:
            for item, description in menu_items.items():
                print(item, "\t", description)  # Display selection menu

            try:
                selection = int(input("\nSelect desired column to analyze:\t"))  # Get user input
                if selection == 1:
                    self.analyze(self.data_frame["Pop Apr 1"], selection)
                elif selection == 2:
                    self.analyze(self.data_frame["Pop Jul 1"], selection)
                elif selection == 3:
                    self.analyze(self.data_frame["Change Pop"], selection)
                elif selection == 4:
                    main_menu()  # Return to main menu
                else:
                    print("\nUse one of the specified choices (1, 2, 3, 4).\n")
            except ValueError:
                print("\nUse one of the specified choices (1, 2, 3, 4).\n")

    def analyze(self, data, selection):
        """
        Analyze the selected data column and print statistics.
        :param data: The data column to analyze.
        :param selection: String for x-axis label, based on user choice
        """
        pop_dict = {
            "\tCount:": data.count(),
            "\tMean:": data.mean(),
            "\tStd Deviation:": data.std(),
            "\tMin:": data.min(),
            "\tMax:": data.max(),
        }

        print("\n", "*" * 40)

        max_key_length = max(len(key) for key, _ in pop_dict.items())

        for key, value in pop_dict.items():
            print(f"{key:<{max_key_length + 1}} {value:10.1f}")  # Format data analysis results

        print("*" * 40, "\n")

        x_label = ""

        try:
            while True:
                choice = input("\nHistogram is available. View now? (Y/N)\t").lower()
                if choice == 'y':
                    if selection == 1:
                        x_label = "Pop Apr 1"
                    elif selection == 2:
                        x_label = "Pop Jul 1"
                    elif selection == 3:
                        x_label = "Change Pop"
                    generate_histogram(data, "PopChangeHistogram", x_label)  # Pass column name
                    break
                elif choice == 'n':
                    break
                else:
                    print("\nInvalid choice. Please use 'Y' or 'N'.\n")
        except ValueError:
            print("\nInvalid choice. Please check.\n")
        finally:
            print("\n")
            self.display_menu()  # Return to selection menu


class Housing:
    """
    This class represents the analysis of housing data.

    It offers methods to analyze various columns of the dataset and display statistics
    including count, mean, standard deviation, min, max, and histograms.
    """
    def __init__(self, data_frame):
        self.data_frame = data_frame

        self.display_menu()  # Display selection menu

    def display_menu(self):
        """
        Display menu to allow user to select a column from the housing data file for analysis.
        """
        menu_items = {
            1: "House Age",
            2: "# Bedrooms",
            3: "Construction Year",
            4: "# Rooms",
            5: "Utility",
            6: "Main Menu",
        }

        while True:
            for item, description in menu_items.items():
                print(item, "\t", description)  # Display selection menu

            try:
                selection = int(
                    input("\nSelect column to analyze:\t")
                )  # Get user input

                if selection == 1:
                    self.analyze(self.data_frame["AGE"], selection)
                elif selection == 2:
                    self.analyze(self.data_frame["BEDRMS"], selection)
                elif selection == 3:
                    self.analyze(self.data_frame["BUILT"], selection)
                elif selection == 4:
                    self.analyze(self.data_frame["ROOMS"], selection)
                elif selection == 5:
                    self.analyze(self.data_frame["UTILITY"], selection)
                elif selection == 6:
                    main_menu()  # Return to main menu
                else:
                    print("\nUse one of the specified choices (1, 2, 3, 4, 5, 6).\n")
            except ValueError:
                print("\nUse one of the specified choices (1, 2, 3, 4, 5, 6).\n")

    def analyze(self, data, selection):
        """
        Analyze the selected data column and print statistics.
        :param data: The data column to analyze.
        :param selection: String for x-axis label, based on user choice
        """
        housing_dict = {
            "\tCount:": data.count(),
            "\tMean:": data.mean(),
            "\tStd Deviation:": data.std(),
            "\tMin:": data.min(),
            "\tMax:": data.max(),
        }

        print("\n", "*" * 40)

        max_key_length = max(len(key) for key, _ in housing_dict.items())

        for key, value in housing_dict.items():
            print(f"{key:<{max_key_length + 1}} {value:10.1f}")  # Format data analysis results

        print("*" * 40, "\n")

        x_label = ""

        try:
            while True:
                choice = input("\nHistogram is available. View now? (Y/N)\t").lower()
                if choice == 'y':
                    if selection == 1:
                        x_label = "House Age"
                    elif selection == 2:
                        x_label = "# Bedrooms"
                    elif selection == 3:
                        x_label = "Construction Year"
                    elif selection == 4:
                        x_label = "# Rooms"
                    elif selection == 5:
                        x_label = "Utility"
                    generate_histogram(data, "HousingHistogram", x_label)  # Pass column name
                    break
                elif choice == 'n':
                    break
                else:
                    print("\nInvalid choice. Please use 'Y' or 'N'.\n")
        except ValueError:
            print("\nInvalid choice. Please check.\n")
        finally:
            print("\n")
            self.display_menu()  # Return to selection menu


if __name__ == "__main__":
    print("SDEV300 Housing and Population Analysis!\n")
    main_menu()
