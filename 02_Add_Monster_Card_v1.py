"""
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

# Create a dictionary for the new Monster Card
# Asking for the Monster Cards name
card_name = input("Enter the name of the new Monster Card: ")
monster_cards_catalogue[card_name] = {}

# Asking for the strength value
strength = input("Enter monster strength (1-25): ")
monster_cards_catalogue[card_name]['strength'] = strength

# Asking for the speed value
speed = input("Enter monster speed (1-25): ")
monster_cards_catalogue[card_name]['speed'] = speed

# Asking for the stealth value
stealth = input("Enter monster stealth (1-25): ")
monster_cards_catalogue[card_name]['stealth'] = stealth

# Asking for the cunning value
cunning = input("Enter monster cunning (1-25): ")
monster_cards_catalogue[card_name]['cunning'] = cunning

# Asking if they want to edit the card
edit = input("do you want to edit the card? ")
if edit == 'yes':
    to_edit = input("What field do you want to edit?: (Monster name, Strength,"
                    " Speed, Stealth, Cunning")
    if to_edit == 'Monster name':
        card_name = input("Enter the name of the new Monster Card: ")
    elif to_edit == 'Strength':
        strength = input("Enter monster strength (1-25): ")
        monster_cards_catalogue[card_name]['strength'] = strength

# Print the Monster Card Catalogue (In format)
for monster_card_name, monster_card_values in monster_cards_catalogue.items():
    print(f"\nMonster Card: {monster_card_name}")

    for key in monster_card_values:
        print(f"{key}: {monster_card_values[key]}")
