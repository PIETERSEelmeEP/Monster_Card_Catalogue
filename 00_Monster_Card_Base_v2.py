"""Took 00_Monster_Card_Base_v1 and added Existing Monster Cards version 3
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

# Welcome message for user
easygui.msgbox("Welcome to Monster Card Catalogue", title="Welcome")
# Ask the user if they want to view the instructions
read_instructions = easygui.buttonbox("Would you like to read the "
                                      "instructions?",
                                      title="Instructions?",
                                      choices=["Yes", "No"])
# Display the instructions
if read_instructions == "Yes":
    easygui.msgbox("Instructions\nThis program catalogues the monster cards"
                   # Explain how to add a monster card & edit it
                   "\n\nIf you wish to add a monster card (Press 'Add')\nThen "
                   "add the monster card details\nIn order of strength, speed,"
                   " stealth, cunning\nAfterwards you will need to confirm the"
                   " values entered are correct\nIf not, continue editing\n\n"
                   # Explain how to search for a monster card & edit it
                   "If you are searching for a monster card to edit it (Press "
                   "'Search')\nThen enter the monster cards name\nThe results "
                   "should display and ask if you want to edit the card\nIf "
                   "yes, start editing\n\n"
                   # Explain how to delete a monster card & verify it
                   "If you want to delete a monster card"
                   " (Press 'Delete')\nThen enter the name of the monster you "
                   "want to delete\nAfterwards you will need to confirm you "
                   "want to delete the monster card\n\nStart cataloging")


# Print the Monster Card Catalogue (In format)
for monster_card_name, monster_card_values in monster_cards_catalogue.items():
    print(f"\nMonster Card: {monster_card_name}")

    for key in monster_card_values:
        print(f"{key}: {monster_card_values[key]}")