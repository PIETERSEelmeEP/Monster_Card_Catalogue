"""This program only consists of creating a welcome message and displaying the
instructions. (Using easygui)
"""

import easygui

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
