"""
John Leckie, SDEV300, 5 September 2023

app.py contains the code for Lab 3. The program presents the user with the capital,
population, and state flower for any selected U.S. State. It allows for display of all
states, a search for a specific state (which additionally displays an image for the
state flower), a bar graph of the 5 most-populated states, and the ability to update
any state's population.
"""

import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.ticker import FuncFormatter

# Dictionary data structure chosen for this application
states_data = [
    {
        "name": "Alabama",
        "capital": "Montgomery",
        "population": 5024279,
        "flower": "Camellia",
    },
    {
        "name": "Alaska",
        "capital": "Juneau",
        "population": 731545,
        "flower": "Forget-Me-Not",
    },
    {
        "name": "Arizona",
        "capital": "Phoenix",
        "population": 7151502,
        "flower": "Saguaro Cactus Blossom",
    },
    {
        "name": "Arkansas",
        "capital": "Little Rock",
        "population": 3011524,
        "flower": "Apple Blossom",
    },
    {
        "name": "California",
        "capital": "Sacramento",
        "population": 39538223,
        "flower": "California Poppy",
    },
    {
        "name": "Colorado",
        "capital": "Denver",
        "population": 5773714,
        "flower": "Columbine",
    },
    {
        "name": "Connecticut",
        "capital": "Hartford",
        "population": 3605944,
        "flower": "Mountain Laurel",
    },
    {
        "name": "Delaware",
        "capital": "Dover",
        "population": 989948,
        "flower": "Peach Blossom",
    },
    {
        "name": "Florida",
        "capital": "Tallahassee",
        "population": 21538187,
        "flower": "Orange Blossom",
    },
    {
        "name": "Georgia",
        "capital": "Atlanta",
        "population": 10711908,
        "flower": "Cherokee Rose",
    },
    {
        "name": "Hawaii",
        "capital": "Honolulu",
        "population": 1455271,
        "flower": "Hawaiian Hibiscus",
    },
    {
        "name": "Idaho",
        "capital": "Boise",
        "population": 1839106,
        "flower": "Syringa",
    },
    {
        "name": "Illinois",
        "capital": "Springfield",
        "population": 12812508,
        "flower": "Violet",
    },
    {
        "name": "Indiana",
        "capital": "Indianapolis",
        "population": 6785528,
        "flower": "Peony",
    },
    {
        "name": "Iowa",
        "capital": "Des Moines",
        "population": 3190369,
        "flower": "Wild Prairie Rose",
    },
    {
        "name": "Kansas",
        "capital": "Topeka",
        "population": 2937880,
        "flower": "Sunflower",
    },
    {
        "name": "Kentucky",
        "capital": "Frankfort",
        "population": 4505836,
        "flower": "Goldenrod",
    },
    {
        "name": "Louisiana",
        "capital": "Baton Rouge",
        "population": 4648794,
        "flower": "Magnolia",
    },
    {
        "name": "Maine",
        "capital": "Augusta",
        "population": 1344212,
        "flower": "White Pine Cone and Tassel",
    },
    {
        "name": "Maryland",
        "capital": "Annapolis",
        "population": 6177224,
        "flower": "Black-Eyed Susan",
    },
    {
        "name": "Massachusetts",
        "capital": "Boston",
        "population": 7029917,
        "flower": "Mayflower",
    },
    {
        "name": "Michigan",
        "capital": "Lansing",
        "population": 10077331,
        "flower": "Dwarf Lake Iris",
    },
    {
        "name": "Minnesota",
        "capital": "St. Paul",
        "population": 5706494,
        "flower": "Pink and White Lady's Slipper",
    },
    {
        "name": "Mississippi",
        "capital": "Jackson",
        "population": 2961279,
        "flower": "Magnolia",
    },
    {
        "name": "Missouri",
        "capital": "Jefferson City",
        "population": 6154913,
        "flower": "Hawthorn",
    },
    {
        "name": "Montana",
        "capital": "Helena",
        "population": 1084259,
        "flower": "Bitterroot",
    },
    {
        "name": "Nebraska",
        "capital": "Lincoln",
        "population": 1961504,
        "flower": "Goldenrod",
    },
    {
        "name": "Nevada",
        "capital": "Carson City",
        "population": 3104614,
        "flower": "Sagebrush",
    },
    {
        "name": "New Hampshire",
        "capital": "Concord",
        "population": 1377529,
        "flower": "Purple Lilac",
    },
    {
        "name": "New Jersey",
        "capital": "Trenton",
        "population": 9288994,
        "flower": "Violet",
    },
    {
        "name": "New Mexico",
        "capital": "Santa Fe",
        "population": 2117522,
        "flower": "Yucca",
    },
    {
        "name": "New York",
        "capital": "Albany",
        "population": 20201249,
        "flower": "Rose",
    },
    {
        "name": "North Carolina",
        "capital": "Raleigh",
        "population": 10439388,
        "flower": "Dogwood",
    },
    {
        "name": "North Dakota",
        "capital": "Bismarck",
        "population": 779094,
        "flower": "Wild Prairie Rose",
    },
    {
        "name": "Ohio",
        "capital": "Columbus",
        "population": 11799448,
        "flower": "Scarlet Carnation",
    },
    {
        "name": "Oklahoma",
        "capital": "Oklahoma City",
        "population": 3959353,
        "flower": "Mistletoe",
    },
    {
        "name": "Oregon",
        "capital": "Salem",
        "population": 4237256,
        "flower": "Oregon Grape",
    },
    {
        "name": "Pennsylvania",
        "capital": "Harrisburg",
        "population": 13002700,
        "flower": "Mountain Laurel",
    },
    {
        "name": "Rhode Island",
        "capital": "Providence",
        "population": 1097379,
        "flower": "Violet",
    },
    {
        "name": "South Carolina",
        "capital": "Columbia",
        "population": 5118425,
        "flower": "Yellow Jessamine",
    },
    {
        "name": "South Dakota",
        "capital": "Pierre",
        "population": 886667,
        "flower": "Pasque Flower",
    },
    {
        "name": "Tennessee",
        "capital": "Nashville",
        "population": 6897576,
        "flower": "Iris",
    },
    {
        "name": "Texas",
        "capital": "Austin",
        "population": 29145505,
        "flower": "Bluebonnet",
    },
    {
        "name": "Utah",
        "capital": "Salt Lake City",
        "population": 3271616,
        "flower": "Sego Lily",
    },
    {
        "name": "Vermont",
        "capital": "Montpelier",
        "population": 643077,
        "flower": "Red Clover",
    },
    {
        "name": "Virginia",
        "capital": "Richmond",
        "population": 8631393,
        "flower": "American Dogwood",
    },
    {
        "name": "Washington",
        "capital": "Olympia",
        "population": 7693612,
        "flower": "Coast Rhododendron",
    },
    {
        "name": "West Virginia",
        "capital": "Charleston",
        "population": 1792147,
        "flower": "Rhododendron",
    },
    {
        "name": "Wisconsin",
        "capital": "Madison",
        "population": 5893718,
        "flower": "Wood Violet",
    },
    {
        "name": "Wyoming",
        "capital": "Cheyenne",
        "population": 567025,
        "flower": "Indian Paintbrush",
    },
]


def display_states():
    """
    Display information about all states.
    """
    # Run through dictionary, formatting output
    for state in states_data:
        print(
            f"State: {state['name']:<15} | Capital: {state['capital']:<15} | "
            f"Population: {state['population']:>10,}   | Flower: {state['flower']:<20}"
        )


def search_state(state_name):
    """
    Search for a state and display its information.

    Arguments taken:
        state_name (string): The name of the desired state.
    """
    for state in states_data:
        if state["name"].lower() == state_name.lower():
            print(
                f"State: {state['name']:<15} | Capital: {state['capital']:<15} | "
                f"Population: {state['population']:>10,}   | Flower: {state['flower']:<20}"
            )

            # Display image of flower
            image_path = f"state_flowers/{state_name.lower()}.jpg"
            try:
                img = Image.open(image_path)
                img.show()
            except FileNotFoundError:
                print(f"Image for {state_name} not found.")

            return
    print("State not found.")


def top_populated_states():
    """
    Display a bar graph of the top 5 populated states.
    """
    top_states = sorted(states_data, key=lambda x: x["population"], reverse=True)[:5]
    state_names = [state["name"] for state in top_states]
    state_populations = [state["population"] for state in top_states]

    plt.bar(state_names, state_populations)
    plt.xlabel("State Name")
    plt.ylabel("Population in Millions")
    plt.title("Top 5 Populated States")

    # Format y-axis ticks to display as '10M', '20M', etc.
    def format_func(value, tick_number):
        if value == 0:
            return ""
        return f"{int(value/1e6)}M"

    plt.gca().get_yaxis().set_major_formatter(FuncFormatter(format_func))
    print(f"Close the graph to proceed!")
    plt.show()


def update_population(state_name):
    """
    Update the population for a state.

    Arguments taken:
        state_name (string): The name of the state to update
    """
    for state in states_data:
        if state["name"].lower() == state_name.lower():
            while True:
                new_population = input(f"Enter new population for {state_name}: ")
                if new_population.isdigit():
                    new_population = int(new_population)
                    if new_population >= 0:
                        state["population"] = new_population
                        print("\nPopulation updated.")
                        print(
                            f"\nState: {state['name']:<15} | Capital: {state['capital']:<15} | "
                            f"Population: {state['population']:>10,}   | Flower: {state['flower']:<20}"
                        )
                        break  # Exit the loop after successful input
                print(
                    "Invalid input. Please enter a non-negative integer for the population."
                )
            return
    print("State not found.")


def get_valid_state_name():
    """
    Helper function for input validation
    Prompt the user for a state name and validate its existence.
    """
    while True:
        state_name = input("Enter state name: ")
        if any(state_name.lower() == state["name"].lower() for state in states_data):
            return state_name
        print("State not found. Please enter a valid state name.")


def main():
    """
    Main program loop that displays the menu and handles user input.
    """
    print(
        "\nWelcome to our U.S. States Information Database!"
        "\nFor any state, we have the capital, population, and state flower"
        "\nto display for you."
    )

    while True:
        print("\nPlease select an option from the menu--")
        print("\nMenu:")
        print("1. Display all states")
        print("2. Search for a state (returns state info and a flower picture)")
        print("3. Top 5 populated states")
        print("4. Update state population")
        print("5. Exit")

        choice = input("Please choose a number (1 to 5): ")

        if choice == "1":
            display_states()
        elif choice == "2":
            state_name = get_valid_state_name()
            search_state(state_name)
        elif choice == "3":
            top_populated_states()
        elif choice == "4":
            state_name = get_valid_state_name()
            update_population(state_name)
        elif choice == "5":
            print("Thank you! Enjoy being more enlightened!")
            break
        else:
            print("Please use 1 through 5.")


if __name__ == "__main__":
    main()
