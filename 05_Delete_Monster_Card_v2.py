"""I took 05_Delete_Monster_Card_v1 and turned it into using easygui and a
function inorder to reuse in further versions
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
cards = list(monster_cards_catalogue.keys())
delete_card = easygui.buttonbox("Select the Monster Card you want to delete",
                                title="Edit Category",
                                choices=cards + ["Exit"])

# Searching for the Monster Card
found = False
for card, value in monster_cards_catalogue.items():
    if delete_card.lower() == card.lower():
        deleted_card = f"Monster Name: {delete_card}\n"
        for category, values in monster_cards_catalogue[delete_card].items():
            deleted_card += f"{category}: {values}\n"
        found = True
        # Asking for confirmation to delete the monster card
        deleted_card += f"Are you sure you want to delete this monster card?"
        confirmation = easygui.buttonbox(f"{deleted_card}",
                                         title="Confirmation",
                                         choices=["Confirm", "Cancel"])
        if confirmation == "Confirm":
            del monster_cards_catalogue[card]
        else:
            continue
        break

if not found:
    easygui.msgbox(f"There are no Combos named {card_search}",
                   title="Not Found")

for monster_card_name, monster_card_values in monster_cards_catalogue \
        .items():
    print(f"\nMonster Card: {monster_card_name}")

    for key in monster_card_values:
        print(f"{key}: {monster_card_values[key]}")
