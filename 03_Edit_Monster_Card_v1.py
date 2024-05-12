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

# Asking if they want to edit the card
edit = input("\nDo you want to edit the card? (yes or no)").lower()
while edit == 'yes':

    # Asking the user what part of the monster card they want to edit
    to_edit = input("What field do you want to edit?: (Strength,"
                    " Speed, Stealth, Cunning, Save or Cancel) ").lower()

    # Allowing them to edit strength value
    if to_edit == 'strength':
        new_strength = input("\nEnter monster strength (1-25): ")

    # Allowing them to edit speed value
    elif to_edit == 'speed':
        new_speed = input("\nEnter monster speed (1-25): ")

    # Allowing them to edit stealth value
    elif to_edit == 'stealth':
        new_stealth = input("\nEnter monster stealth (1-25): ")

    # Allowing them to edit cunning value
    elif to_edit == 'cunning':
        new_cunning = input("\nEnter monster cunning (1-25): ")

    # Allowing them to save their edits
    elif to_edit == 'save':
        monster_cards_catalogue[card_name]['new_strength'] = strength
        monster_cards_catalogue[card_name]['new_speed'] = speed
        monster_cards_catalogue[card_name]['new_stealth'] = stealth
        monster_cards_catalogue[card_name]['new_cunning'] = cunning
        break

    # Allowing them to cancel/delete their edits
    else:
        confirm = input("\nAre you sure you want to cancel? (yes or no) ")\
            .lower()
        if confirm == 'yes':
            break
        else:
            continue

