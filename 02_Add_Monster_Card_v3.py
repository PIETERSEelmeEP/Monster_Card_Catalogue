"""This program is the same as 02_Add_Monster_Card_v2, however, instead of
using the python console, this program uses easygui. Due to easygui containing
upper and lower bounds, there is no purpose for the value checker function,
so we can remove it
"""

import easygui

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


# Create a new monster card function
def create_new_monster_card():
    # Create a dictionary for the new Monster Card
    # Asking for the Monster Cards name
    card_name = easygui.enterbox("Enter the name of the new Monster Card: ",
                                 title="Monster Card Name")
    monster_cards_catalogue[card_name] = {}

    # Asking for the strength value
    strength = easygui.integerbox("Enter monster strength (1-25)",
                                  title="Strength Value", lowerbound=1,
                                  upperbound=25)
    monster_cards_catalogue[card_name]['Strength'] = strength

    # Asking for the speed value
    speed = easygui.integerbox("Enter monster speed (1-25)",
                               title="Speed Value", lowerbound=1,
                               upperbound=25)
    monster_cards_catalogue[card_name]['Speed'] = speed

    # Asking for the stealth value
    stealth = easygui.integerbox("Enter monster stealth (1-25)",
                                 title="Stealth Value", lowerbound=1,
                                 upperbound=25)
    monster_cards_catalogue[card_name]['Stealth'] = stealth

    # Asking for the cunning value
    cunning = easygui.integerbox("Enter monster cunning (1-25)",
                                 title="Cunning Value", lowerbound=1,
                                 upperbound=25)
    monster_cards_cat2alogue[card_name]['Cunning'] = cunning


# Main Routine
create_new_monster_card()

# Print the Monster Card Catalogue (In format) in python console
for monster_card_name, monster_card_values in monster_cards_catalogue.items():
    print(f"\nMonster Card: {monster_card_name}")

    for key in monster_card_values:
        print(f"{key}: {monster_card_values[key]}")
