"""In this version the program will display all the monster cards and the user
can select the monster card they are searching for.
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

# Main Routine
catalogue = monster_cards_catalogue[:]
card_search = easygui.choicebox("Select the Monster Card you are searching for"
                                , title="Searching",
                                choices=catalogue)

# Searching for the Monster Card name
found = False
for card, values in monster_cards_catalogue.items():
    if card_search.lower() == card.lower():
        print("Results:")
        print(f"Monster Name: {card_search}")
        for category, level in values.items():
            print(f"{category}: {level}")
        found = True
        break
    else:
        for level in values:
            if card_search.lower() == level.lower():
                print("Results:")
                print(f"Monster Name: {card_search}")
                for category, level_ in values.items():
                    print(f"{category}: {level_}")
                found = True
        break

if not found:
    print(f"There are no Monster Card named {card_search}\nNor are there any "
          f"category's within Monster cards with the value of {card_search}")
