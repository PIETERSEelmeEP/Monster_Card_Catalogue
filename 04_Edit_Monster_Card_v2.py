"""This program asks the user to select the Monster card then category they
want to edit, then allow them to enter the new value, and either save or cancel
the newly entered values (using easygui)
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

# Asking what monster card they want to edit
catalogue = list(monster_cards_catalogue.keys())
edit_card = easygui.buttonbox("Select the Monster Card you want to edit",
                              title="Searching",
                              choices=catalogue + ["Cancel"])

if edit_card and edit_card != "Cancel":
    while True:
        categories = list(monster_cards_catalogue[edit_card].keys())
        original_values = f"Monster Name: {edit_card}\n"
        for category, values in monster_cards_catalogue[edit_card].items():
            original_values += f"{category}: {values}\n"
        new_category = easygui.buttonbox(f"{original_values}\nSelect the "
                                         f"category you want to edit:",
                                         title="Edit Category",
                                         choices=categories + ["Exit"])
        if new_category and new_category != "Exit":

            new_value = easygui.integerbox(f"Enter the new value for "
                                           f"{new_category} (1-25):",
                                           title="New Value",
                                           lowerbound=1,
                                           upperbound=25)
            if new_value is not None:
                # Update the value in the catalogue
                monster_cards_catalogue[edit_card][new_category] = new_value

                # Display the newly edited monster card's values
                new_values = f"Monster Name: {edit_card}\n"
                for category, values in monster_cards_catalogue[edit_card]\
                        .items():
                    new_values += f"{category}: {values}\n"
                new_values += "Would you like to save these changes or cancel?"

                save_new_value = easygui.buttonbox(new_values,
                                                   title="Save Changes",
                                                   choices=["Save", "Cancel"])
                if save_new_value == "Save":
                    easygui.msgbox("Changes saved successfully!",
                                   title="Success")
                else:
                    cancel = easygui.buttonbox("Are you sure you want to "
                                               "cancel?",
                                               title="Cancel Confirmation",
                                               choices=["Yes", "No"])
                    if cancel == "Yes":
                        # Reset the edited value
                        monster_cards_catalogue[edit_card][new_category] = \
                            new_value
                        easygui.msgbox("Changes cancelled.", title="Cancelled")
        else:
            break

for monster_card_name, monster_card_values in monster_cards_catalogue.items():
    print(f"\nMonster Card: {monster_card_name}")

    for key in monster_card_values:
        print(f"{key}: {monster_card_values[key]}")
