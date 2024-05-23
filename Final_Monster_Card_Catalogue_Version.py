"""Took 00_Monster_Card_Base_v6 and edited it and added a goodbye message
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
    monster_cards_catalogue[card_name]['Cunning'] = cunning


# Edit a selected Monster Card Function
def edit_monster_card(edit_card):
    if edit_card != "Cancel":
        while True:
            # Display the original Monster Card Values
            categories = list(monster_cards_catalogue[edit_card].keys())
            original_values = f"Monster Name: {edit_card}\n"
            for category, values in monster_cards_catalogue[edit_card].items():
                original_values += f"{category}: {values}\n"
            # Ask user what category they want to edit
            new_category = easygui.buttonbox(f"{original_values}\nSelect the "
                                             f"category you want to edit:",
                                             title="Edit Category",
                                             choices=categories + ["Exit"])
            if new_category != "Exit":
                # Input the new value for the category selected
                new_value = easygui.integerbox(f"Enter the new value for "
                                               f"{new_category} (1-25):",
                                               title="New Value",
                                               lowerbound=1,
                                               upperbound=25)
                if new_value is not None:
                    # Display the newly edited monster card's values
                    new_values = f"Monster Name: {edit_card}\n"
                    for category, values in monster_cards_catalogue[edit_card]\
                            .items():
                        new_values += f"{category}: {values}\n"
                    new_values += f"New Edited Version:\n"
                    new_values += f"{new_category}: {new_value}\n"
                    # Ask for confirmation that value is correct (save or not)
                    new_values += "Would you like to save these changes or " \
                                  "cancel?"

                    save_new_value = easygui.buttonbox(new_values,
                                                       title="Save Changes",
                                                       choices=["Save",
                                                                "Cancel"])
                    if save_new_value == "Save":
                        # Update the value in the catalogue
                        monster_cards_catalogue[edit_card][new_category] = \
                            new_value
                        easygui.msgbox("Changes saved successfully!",
                                       title="Success")
                    # Ask for confirmation to delete the newly input value
                    else:
                        cancel = easygui.buttonbox("Are you sure you want to "
                                                   "cancel?",
                                                   title="Cancel Confirmation",
                                                   choices=["Yes", "No"])
                        # Delete new value, keep the original unchanged
                        if cancel == "Yes":
                            # Reset the edited value
                            easygui.msgbox("Changes cancelled.",
                                           title="Cancelled")
            else:
                break


# Search for Monster Card Function
def search_monster_card():
    catalogue = list(monster_cards_catalogue)
    # User selects monster card they are searching for
    card_search = easygui.buttonbox("Select the Monster Card you are searching"
                                    " for", title="Searching",
                                    choices=catalogue + ["Cancel"])

    # Print the Results
    search_results = ""
    if card_search == "Cancel":
        return card_search
    elif card_search:
        search_results += f"Monster Name: {card_search}\n"
        for category, values in monster_cards_catalogue[card_search].items():
            search_results += f"{category}: {values}\n"
        proceed = easygui.buttonbox(search_results, title="Results",
                                    choices=["Edit", "Print", "Exit"])
        if proceed == "Edit":
            # Asking what monster card they want to edit
            catalogue = list(monster_cards_catalogue.keys())
            edit_card = easygui.buttonbox(
                "Select the Monster Card you want to edit",
                title="Searching",
                choices=catalogue + ["Cancel"])
            edit_monster_card(edit_card)
        elif proceed == "Print":
            print(search_results)
    else:
        easygui.msgbox("No card selected!", title="Results")


# Delete monster card function
def delete_monster_card():
    while True:
        # Ask user to select monster card they want to delete
        cards = list(monster_cards_catalogue.keys())
        delete_card = easygui.buttonbox(
            "Select the Monster Card you want to delete",
            title="Delete Monster Card",
            choices=cards + ["Exit"])

        # Searching for the Monster Card
        if delete_card != "Exit":
            for card, value in monster_cards_catalogue.items():
                if delete_card.lower() == card.lower():
                    # Display the monster card to verify
                    deleted_card = f"Monster Name: {delete_card}\n"
                    for category, values in \
                            monster_cards_catalogue[delete_card].items():
                        deleted_card += f"{category}: {values}\n"
                    # Asking for confirmation to delete the monster card
                    deleted_card += f"Are you sure you want to delete this " \
                                    f"monster card?"
                    confirmation = easygui.buttonbox(f"{deleted_card}",
                                                     title="Confirmation",
                                                     choices=["Confirm",
                                                              "Cancel"])
                    if confirmation == "Confirm":
                        # Delete Monster card permanently from catalogue
                        del monster_cards_catalogue[card]
                        easygui.msgbox("Monster Card successfully deleted",
                                       title="Confirmed")
                    else:
                        # Keep the monster card unchanged in catalogue
                        easygui.msgbox("Deletion cancelled", title="Complete")
                        continue
                    break
        # If user selects exit break loop and exit function
        else:
            break


# Main Routine
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
                   "want to delete the monster card\n"
                   # Exit and print full monster card catalogue
                   "If you want to exit the program (Press 'Print Catalogue') "
                   "Then the entire monster card catalogue will be printed in "
                   "the python console. And the program will end\n\nStart "
                   "cataloging")

while True:
    option = easygui.buttonbox("Select further action", title="Main Dialogue",
                               choices=["Add", "Search", "Edit", "Delete",
                                        "Print Catalogue"])

    # Activate the action the user selects
    if option == "Add":
        # Activate the new monster card function
        create_new_monster_card()
    elif option == "Search":
        # Activate the search monster card function
        search_monster_card()
    elif option == "Edit":
        # Activate the edit monster card function
        edit_monster_card()
    elif option == "Delete":
        delete_monster_card()
    else:
        # Print the Monster Card Catalogue (In format) in python console
        for monster_card_name, monster_card_values in monster_cards_catalogue \
                .items():
            print(f"\nMonster Card: {monster_card_name}")

            for key in monster_card_values:
                print(f"{key}: {monster_card_values[key]}")
        easygui.msgbox("Farewell", title="Farewell Message")
        break
