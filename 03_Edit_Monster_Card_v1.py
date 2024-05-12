edit = input("\nDo you want to edit the card? (yes or no)").lower()
while edit == 'yes':

    # Asking the user what part of the monster card they want to edit
    to_edit = input("What field do you want to edit?: (Strength,"
                    " Speed, Stealth, Cunning, Save or Cancel) ").lower()

    # Allowing them to edit strength value
    if to_edit == 'strength':
        new_strength = int(input("\nEnter monster strength (1-25): "))
        monster_cards_catalogue[card_name]['Strength'] = \
            value_checker(new_strength)

    # Allowing them to edit speed value
    elif to_edit == 'speed':
        new_speed = int(input("\nEnter monster speed (1-25): "))
        monster_cards_catalogue[card_name]['Speed'] = \
            value_checker(new_speed)

    # Allowing them to edit stealth value
    elif to_edit == 'stealth':
        new_stealth = int(input("\nEnter monster stealth (1-25): "))
        monster_cards_catalogue[card_name]['Stealth'] = \
            value_checker(new_stealth)

    # Allowing them to edit cunning value
    elif to_edit == 'cunning':
        new_cunning = int(input("\nEnter monster cunning (1-25): "))
        monster_cards_catalogue[card_name]['Cunning'] = \
            value_checker(new_cunning)

    # Allowing them to save their edits
    elif to_edit == 'save':
        print("Edits saved!")
        break

    # Allowing them to cancel/delete their edits
    else:
        confirm = input("\nAre you sure you want to cancel? (yes or no) ")\
            .lower()
        if confirm == 'yes':
            break
        else:
            continue