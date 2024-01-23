"""
John Leckie, SDEV 300, Lab 1

lab1_leckie_john takes appropriate voter registration info, verifying that each
entry meets requirements.
"""

def get_valid_input(prompt, validator_func):
    """
    This function grabs user input and validates it according to what
    entry is currently being worked on.
    """
    while True:
        user_input = input(prompt)
        if validator_func(user_input):
            return user_input
        print('Input invalid for this field. Please try again.')


def validate_name(name):
    """
    Validate whether the input name consists of only alphabetic characters.
    """
    return name.isalpha()


def validate_age(age):
    """
    Validate whether the input age is a nonzero, non-negative integer between 1 and 100.
    """
    try:
        age = int(age)
        return 0 < age < 101
    except ValueError:
        return False


def validate_country(country):
    """
    Validate whether the input country consists of only alphabetic characters.
    """
    return country.isalpha()


def validate_state(state):
    """
    Validate whether the input state is a valid two-letter state code.
    """
    valid_states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL",
                    "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT",
                    "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI",
                    "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    return state.upper() in valid_states


def validate_zipcode(zipcode):
    """
    Validate whether the input zipcode is a 5-digit numerical value.
    """
    return len(zipcode) == 5 and zipcode.isdigit()


def main():
    """
    This is the main function that handles voter registration.
    It gathers and validates user input for voter registration fields.
    """
    print("***Totally Rigged Voter Registration Application!***\n")

    first_name = get_valid_input("First name (alphabetic only): ", validate_name)
    last_name = get_valid_input("Last name (alphabetic only): ", validate_name)
    age = get_valid_input("Age (1 to 100): ", validate_age)
    age = int(age)
    country = get_valid_input("Country of citizenship (2-letter code): ", validate_country)

    if age >= 18 and country.lower() == "us":
        state = get_valid_input("State of residence (2-letter code): ", validate_state)
        zipcode = get_valid_input("5-digit zipcode (numeric only): ", validate_zipcode)

        print("\nCongratulations! You are registered! To confirm: ")
        print("Voter Registration Summary:")
        print(f"Name: {first_name} {last_name}")
        print(f"Age: {age}")
        print(f"Country: {country}")
        print(f"State: {state}")
        print(f"Zipcode: {zipcode}")
    else:
        print("\nYou are not eligible to vote.")


if __name__ == "__main__":
    main()
