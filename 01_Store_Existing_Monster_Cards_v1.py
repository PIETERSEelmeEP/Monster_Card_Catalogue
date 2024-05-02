"""First Trial of storing the existing Monster Cards. This version will be
using a dictionary within a list
"""
# Monster Card Catalogue using a dictionary in lists
monster_cards_catalogue = [
    ["Stoneling", {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15}],
    ["Vexscream", {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19}],
    ["Dawnmirage", {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22}],
    ["Blazegolem", {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6}],
    ["Websnake", {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5}],
    ["Moldvine", {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5}],
    ["Vortexwing", {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2}],
    ["Rotthing", {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12}],
    ["Froststep", {"Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4}],
    ["Wispghoul", {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 4}]
]

# Print the Monster Card Catalogue (In format)
for monster_cards in monster_cards_catalogue:
    monster_card_name = monster_cards[0]
    monster_card_value = monster_cards[1]
    print(f"\nMonster Card: {monster_card_name}")
    for categories, value in monster_card_value.items():
        print(f"\t{categories}: {value}")
