"""Second Trial of storing the existing Monster Cards. This version will be
using dictionaries within a list instead of using a single dictionary within a
list
"""
# Monster Card Catalogue using a dictionaries in a list
monster_cards_catalogue = [
    {"Card Name": "Stoneling", "Statistics":
        {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15}},
    {"Card Name": "Vexscream", "Statistics":
        {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19}},
    {"Card Name": "Dawnmirage", "Statistics":
        {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22}},
    {"Card Name": "Blazegolem", "Statistics":
        {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6}},
    {"Card Name": "Websnake", "Statistics":
        {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5}},
    {"Card Name": "Moldvine", "Statistics":
        {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5}},
    {"Card Name": "Vortexwing", "Statistics":
        {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2}},
    {"Card Name": "Rotthing", "Statistics":
        {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12}},
    {"Card Name": "Froststep", "Statistics":
        {"Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4}},
    {"Card Name": "Wispghoul", "Statistics":
        {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 4}}
]

# Print the Monster Card Catalogue (In format)
for monster_cards in monster_cards_catalogue:
    monster_card_name = monster_cards["Card Name"]
    monster_card_value = monster_cards["Statistics"]
    print(f"\nMonster Card: {monster_card_name}")
    for categories, value in monster_card_value.items():
        print(f"\t{categories}: {value}")
