"""This program asks the user to select the Monster card then category they
want to edit, then allow them to enter the new value, and either save or cancel
the newly entered values
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

# Asking what monster card they want to edit
print("\nMonster Cards Catalogue:")
for monster_card_name in monster_cards_catalogue:
    print(f"{monster_card_name}")

edit_card = input("\nEnter the monster card you would like to edit: ").title()

if edit_card not in monster_cards_catalogue:
    print("Invalid monster card name. Exiting program.")
else:
    card = monster_cards_catalogue[edit_card]

    while True:
        print(f"\nEditing {edit_card}:")
        for key, value in card.items():
            print(f"{key}: {value}")

        to_edit = input("What field do you want to edit? (Strength, Speed, "
                        "Stealth, Cunning, Save, or Cancel): ").title()

        if to_edit == 'Save':
            print(f"Changes to {edit_card} have been saved.")
            break
        elif to_edit == 'Cancel':
            confirm = input("Are you sure you want to cancel? (yes or no): ")\
                .lower()
            if confirm == 'yes':
                print("No changes were made.")
                break
        elif to_edit in card:
            try:
                new_value = int(input(f"Enter new {to_edit} value (1-25): "))
                if 1 <= new_value <= 25:
                    card[to_edit] = new_value
                else:
                    print("Value out of range. Please enter a value between 1 "
                          "and 25.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        else:
            print("Invalid field. Please choose from Strength, Speed, Stealth,"
                  " Cunning, Save, or Cancel.")

for monster_card_name, monster_card_values in monster_cards_catalogue.items():
    print(f"\nMonster Card: {monster_card_name}")

    for key in monster_card_values:
        print(f"{key}: {monster_card_values[key]}")
