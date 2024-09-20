import random
from main import weapon, strength, strength_mod, dex, dex_mod, con, con_mod, intelligence, intelligence_mod, wis, wis_mod, cha, cha_mod

def innkeeper():
    hp = 10
    hit_roll = random.randint(1, 20)
    damage_roll = random.randint(1, 20) + strength_mod if weapon == False else damage_roll = random.randint()

    if hit_roll >= 10:
        print(f"You rolled {hit_roll} and land a hit on the innkeeper.")