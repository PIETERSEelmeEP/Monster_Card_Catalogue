"""This program will ask the user to enter a monster card they would like to
delete and verify that choice
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

# Main Routine
delete_card = input("Enter the name of the Monster card you want to delete: ")

# Searching for the Monster Card
found = False
for card, values in monster_cards_catalogue.items():
    if delete_card.lower() == card.lower():
        print("Results:")
        print(f"Monster Name: {delete_card}")
        for category, level in values.items():
            print(f"{category}: {level}")
        found = True
        # Asking for confirmation to delete the monster card
        confirmation = input("Are you sure you want to delete this monster "
                             "card? (Enter yes or no)").lower()
        if confirmation == "yes":
            del monster_cards_catalogue[delete_card].lower
        else:
            continue
        break

if not found:
    print(f"There are no Combos named {card_search}")
