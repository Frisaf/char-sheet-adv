import random
from main import full_name

def set_scores():
    print(f"Let's continue by setting your {full_name}'s stats!")
    input("Press ENTER to determine your strength.")

    strength1 = random.randint(1, 6)
    strength2 = random.randint(1, 6)
    strength3 = random.randint(1, 6)
    strength4 = random.randint(1, 6)

    print(f"You rolled: {strength1}, {strength2}, {strength3}, {strength4}")

    strength_min = min([strength1, strength2, strength3, strength4])

    print(f"Removing {strength_min} as it is the lowest roll.")

    strength = strength1 + strength2 + strength3 + strength4 - strength_min

    print(f"Your strength score is {strength}")

    if strength == 3:
        strength_mod = -4
    
    elif strength in(4, 5):
        strength_mod = -3
    
    elif strength in(6, 7):
        strength_mod = -2
    
    elif strength in(8, 9):
        strength_mod = -1
    
    elif strength in(10, 11):
        strength_mod = 0
    
    elif strength in(12, 13):
        strength_mod = 1
    
    elif strength in(14, 15):
        strength_mod = 2
    
    elif strength in(16, 17):
        strength_mod = 3
    
    elif strength == 18:
        strength_mod = 4
    
    print(f"This means that your strength modifier is {strength_mod}")
    input("Press ENTER to continue.\n")
    
    dex1 = random.randint(1, 6)
    dex2 = random.randint(1, 6)
    dex3 = random.randint(1, 6)
    dex4 = random.randint(1, 6)

    print(f"You rolled: {dex1}, {dex2}, {dex3}, {dex4}")

    dex_min = min([dex1, dex2, dex3, dex4])

    print(f"Removing {dex_min} as it is the lowest roll")

    dex = dex1 + dex2 + dex3 + dex4 - dex_min

    print(f"Your dexterity score is {dex}")

    if dex == 3:
        dex_mod = -4
    
    elif dex in(4, 5):
        dex_mod = -3
    
    elif dex in(6, 7):
        dex_mod = -2
    
    elif dex in(8, 9):
        dex_mod = -1
    
    elif dex in(10, 11):
        dex_mod = 0
    
    elif dex in(12, 13):
        dex_mod = 1
    
    elif dex in(14, 15):
        dex_mod = 2
    
    elif dex in(16, 17):
        dex_mod = 3
    
    elif dex == 18:
        dex_mod = 4

    print(f"This means that your dexterity modifier is {dex_mod}")
    input("Press ENTER to continue.\n")

    con1 = random.randint(1, 6)
    con2 = random.randint(1, 6)
    con3 = random.randint(1, 6)
    con4 = random.randint(1, 6)

    print(f"You rolled: {con1}, {con2}, {con3}, {con4}")

    con_min = min([con1, con2, con3, con4])

    print(f"Removing {con_min} as it is the lowest roll.")

    con = con1 + con2 + con3 + con4 - con_min

    print(f"Your constitution score is {con}")

    if con == 3:
        con_mod = -4
    
    elif con in(4, 5):
        con_mod = -3
    
    elif con in(6, 7):
        con_mod = -2
    
    elif con in(8, 9):
        con_mod = -1
    
    elif con in(10, 11):
        con_mod = 0
    
    elif con in(12, 13):
        con_mod = 1
    
    elif con in(14, 15):
        con_mod = 2
    
    elif con in(16, 17):
        con_mod = 3
    
    elif con == 18:
        con_mod = 4

    print(f"This means that your constitution modifier is {con_mod}")

    intelligence1 = random.randint(1, 6)
    intelligence2 = random.randint(1, 6)
    intelligence3 = random.randint(1, 6)
    intelligence4 = random.randint(1, 6)

    print(f"You rolled: {intelligence1}, {intelligence2}, {intelligence3}, {intelligence4}")

    intelligence_min = min([intelligence1, intelligence2, intelligence3, intelligence4])

    print(f"Removing {intelligence_min} as it is the lowest roll.")

    intelligence = intelligence1 + intelligence2 + intelligence3 + intelligence4 - intelligence_min

    print(f"Your constitution score is {intelligence}")

    if intelligence == 3:
        intelligence_mod = -4
    
    elif intelligence in(4, 5):
        intelligence_mod = -3
    
    elif intelligence in(6, 7):
        intelligence_mod = -2
    
    elif intelligence in(8, 9):
        intelligence_mod = -1
    
    elif intelligence in(10, 11):
        intelligence_mod = 0
    
    elif intelligence in(12, 13):
        intelligence_mod = 1
    
    elif intelligence in(14, 15):
        intelligence_mod = 2
    
    elif intelligence in(16, 17):
        intelligence_mod = 3
    
    elif intelligence == 18:
        intelligence_mod = 4

    print(f"This means that your constitution modifier is {intelligence_mod}")
    input("Press ENTER to continue.\n")

    wis1 = random.randint(1, 6)
    wis2 = random.randint(1, 6)
    wis3 = random.randint(1, 6)
    wis4 = random.randint(1, 6)

    print(f"You rolled: {wis1}, {wis2}, {wis3}, {wis4}")

    wis_min = min([wis1, wis2, wis3, wis4])

    print(f"Removing {wis_min} as it is the lowest roll.")

    wis = wis1 + wis2 + wis3 + wis4 - wis_min

    print(f"Your constitution score is {wis}")

    if wis == 3:
        wis_mod = -4
    
    elif wis in(4, 5):
        wis_mod = -3
    
    elif wis in(6, 7):
        wis_mod = -2
    
    elif wis in(8, 9):
        wis_mod = -1
    
    elif wis in(10, 11):
        wis_mod = 0
    
    elif wis in(12, 13):
        wis_mod = 1
    
    elif wis in(14, 15):
        wis_mod = 2
    
    elif wis in(16, 17):
        wis_mod = 3
    
    elif wis == 18:
        wis_mod = 4

    print(f"This means that your constitution modifier is {wis_mod}")