"""I took 03_Search_for_Monster_Card_v5 and converted it into a function to
allow the program to be reused
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


# Search for Monster Card Function
def search_monster_card():
    catalogue = list(monster_cards_catalogue)
    # User selects monster card they are searching for
    card_search = easygui.buttonbox("Select the Monster Card you are searching"
                                    " for", title="Searching",
                                    choices=catalogue)

    # Print the Results
    search_results = ""
    if card_search:
        search_results += f"Monster Name: {card_search}\n"
        for category, values in monster_cards_catalogue[card_search].items():
            search_results += f"{category}: {values}\n"
        easygui.msgbox(search_results, title="Results")
    else:
        easygui.msgbox("No card selected!", title="Results")


# Main Routine
search_monster_card()