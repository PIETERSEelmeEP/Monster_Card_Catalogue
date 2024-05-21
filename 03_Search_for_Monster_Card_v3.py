"""Taking 03_Search_for_Monster_Card_v2 and changing it to easygui
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
card_search = easygui.enterbox("Enter the name of the Monster card you are "
                               "searching for", title="Searching")

# Searching for the Monster Card name or its value
found = False
search_results = "Results\n"

for card, values in monster_cards_catalogue.items():
    if card_search.lower() == card.lower():
        search_results += f"Monster Name: {card}\n"
        for category, level in values.items():
            search_results += f"{category}: {level}\n"
        found = True
        break
    else:
        for category, level in values.items():
            if str(level).lower() == card_search.lower():
                search_results += f"Monster Name: {card}\n"
                for category_, level_ in values.items():
                    search_results += f"{category_}: {level_}\n"
                found = True
                break
        if found:
            break

if found:
    easygui.msgbox(search_results, title="Results")
else:
    easygui.msgbox(f"There are no Monster Cards named '{card_search}'\nNor are"
                   f" there any categories within Monster cards with the value"
                   f" of '{card_search}'", title="Results")
#
# card_search = easygui.enterbox("Enter the name of the Monster card you are "
#                                "searching for", title="Searching")
#
# # Searching for the Monster Card name or its value
# found = False
# search_results = "Results\n"
# for card, values in monster_cards_catalogue.items():
#     if card_search.lower() == card.lower():
#         search_results += f"Monster Name: {card_search}\n"
#         for category, level in values.items():
#             search_results += f"{category}: {values}\n"
#         found = True
#         break
#     else:
#         for catagory, level in values.items():
#             if str(level).lower() == card_search.lower():
#                 search_results += f"Monster Name: {card_search}\n"
#                 for category, level_ in values.items():
#                     search_results += f"{category}: {values}\n"
#                 found = True
#                 break
# easygui.msgbox(search_results, title="Results")
#
# if not found:
#     easygui.msgbox(f"There are no Monster Card named {card_search}\nNor are "
#                    f"there any category's within Monster cards with the value "
#                    f"of {card_search}", title="Results")
