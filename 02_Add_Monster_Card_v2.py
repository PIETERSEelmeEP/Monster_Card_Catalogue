"""This program only uses the python console. This program asks the user if
they want to  create a new monster card. Boundaries are set unlike
02_Add_Monster_Card_v1, and I made it a function allowing for it to be reused.
"""

# Monster Card Catalogue using dictionaries within nested dictionaries
monster_cards_catalogue = {
    "Stoneling": {
        "Strength": 7,
        "Speed": 1,
        "Stealth": 25,
        "Cunning": 15
    },
    "Vexscream": {
        "Strength": 1,
        "Speed": 6,
        "Stealth": 21,
        "Cunning": 19
    },
    "Dawnmirage": {
        "Strength": 5,
        "Speed": 15,
        "Stealth": 18,
        "Cunning": 22
    },
    "Blazegolem": {
        "Strength": 15,
        "Speed": 20,
        "Stealth": 23,
        "Cunning": 6
    },
    "Websnake": {
        "Strength": 7,
        "Speed": 15,
        "Stealth": 10,
        "Cunning": 5
    },
    "Moldvine": {
        "Strength": 21,
        "Speed": 18,
        "Stealth": 14,
        "Cunning": 5
    },
    "Vortexwing": {
        "Strength": 19,
        "Speed": 13,
        "Stealth": 19,
        "Cunning": 2
    },
    "Rotthing": {
        "Strength": 16,
        "Speed": 7,
        "Stealth": 4,
        "Cunning": 12
    },
    "Froststep": {
        "Strength": 14,
        "Speed": 14,
        "Stealth": 17,
        "Cunning": 4
    },
    "Wispghoul": {
        "Strength": 17,
        "Speed": 19,
        "Stealth": 3,
        "Cunning": 4
    }
}


# Check value is within boundaries
def value_checker(value):
    if not (1 <= value <= 25):
        print("Please enter a value between 1 and 25")
        value = int(input("\nEnter value (1-25): "))
    return value


# Create a new monster card function
def create_new_monster_card():
    # Create a dictionary for the new Monster Card
    # Asking for the Monster Cards name
    card_name = input("\nEnter the name of the new Monster Card: ")
    monster_cards_catalogue[card_name] = {}

    # Asking for the strength value
    strength = int(input("\nEnter monster strength (1-25): "))
    strength = value_checker(strength)
    monster_cards_catalogue[card_name]['Strength'] = strength

    # Asking for the speed value
    speed = int(input("\nEnter monster speed (1-25): "))
    speed = value_checker(speed)
    monster_cards_catalogue[card_name]['Speed'] = speed

    # Asking for the stealth value
    stealth = int(input("\nEnter monster stealth (1-25): "))
    stealth = value_checker(stealth)
    monster_cards_catalogue[card_name]['Stealth'] = stealth

    # Asking for the cunning value
    cunning = int(input("\nEnter monster cunning (1-25): "))
    cunning = value_checker(cunning)
    monster_cards_catalogue[card_name]['Cunning'] = cunning


# Main Routine
create_new_monster_card()

# Print the Monster Card Catalogue (In format)
for monster_card_name, monster_card_values in monster_cards_catalogue.items():
    print(f"\nMonster Card: {monster_card_name}")

    for key in monster_card_values:
        print(f"{key}: {monster_card_values[key]}")
