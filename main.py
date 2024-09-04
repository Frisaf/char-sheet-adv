import random, time

first_names = [
    "Phraan",
    "Ardeth",
    "Alred",
    "Kivessin",
    "Elluin",
    "Evindal",
    "Elas",
    "Wyn",
    "Taeral",
    "Eltaor",
]

last_names = [
    "Zylralei",
    "Inaroris",
    "Keymenor",
    "Paric",
    "Xilhorn",
    "Iarceran",
    "Trawarin",
    "Erhorn",
    "Phizorwyn",
    "Reykian",
]

modifiers = {
    range(3, 4): -4,
    range(4, 6): -3,
    range(6, 8): -2,
    range(8, 10): -1,
    range(10, 12): 0,
    range(12, 14): 1,
    range(14, 16): 2,
    range(16, 18): 3,
    range(18, 19): 4,
}

def startup():
    while True:
        print("Welcome, adventurer! Let's start with making a character sheet.")
        name = input("What is your character's name? Type 'ran' to get a random name.\n> ").lower()

        if name == "ran":
            global full_name

            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            full_name = f"{first_name} {last_name}"

            print(f"Your character's name is {full_name}")
        
        else:
            print(f"Your character's name is {name}")
        
        proceed_ans = input(f"Looks good, {full_name}? Type yes or no.\n> ").lower()

        if proceed_ans == "yes":
            set_scores()
            break
        
        elif proceed_ans == "no":
            continue
        else:
            print("Please answer yes or no.")

def set_scores():
    print(f"Let's roll your ability scores!")
    input("Press ENTER to continue.")

    rolls = [random.randint(1, 6) for _ in range(4)]

    print(f"You rolled: {', '.join(map(str, rolls))}")

    strength = sum(rolls) - min(rolls)
    strength_mod = next(mod for rng, mod in modifiers.items() if strength in rng)

    time.sleep(1)

    print(f"Removing {min(rolls)} as it is the lowest roll.")
    time.sleep(1)
    print(f"Your strength score is {strength}.")
    time.sleep(1)
    print(f"This means that your strength modifier is {strength_mod}.")
    input("Press ENTER to continue.")

    rolls = [random.randint(1, 6) for _ in range(4)]

    print(f"You rolled: {', '.join(map(str, rolls))}")

    dex = sum(rolls) - min(rolls)
    dex_mod = next(mod for rng, mod in modifiers.items() if dex in rng)

    time.sleep(1)

    print(f"Removing {min(rolls)} as it is the lowest roll.")
    time.sleep(1)
    print(f"Your dexterity score is {dex}")
    time.sleep(1)
    print(f"This means that your dexterity modifier is {dex_mod}")
    input("Press ENTER to continue.")

    rolls = [random.randint(1, 6) for _ in range(4)]

    print(f"You rolled: {', '.join(map(str, rolls))}")

    con = sum(rolls) - min(rolls)
    con_mod = next(mod for rng, mod in modifiers.items() if con in rng)

    time.sleep(1)

    print(f"Removing {min(rolls)} as it is the lowest roll.")
    time.sleep(1)
    print(f"Your constitution score is {con}")
    time.sleep(1)
    print(f"This means that your constitution modifier is {con_mod}")
    input("Press ENTER to continue.")

    rolls = [random.randint(1, 6) for _ in range(4)]

    print(f"You rolled: {', '.join(map(str, rolls))}")

    intelligence = sum(rolls) - min(rolls)
    intelligence_mod = next(mod for rng, mod in modifiers.items() if intelligence in rng)

    time.sleep(1)
    
    print(f"Removing {min(rolls)} as it is the lowest roll.")
    time.sleep(1)
    print(f"Your intelligence score is {intelligence}.")
    time.sleep(1)
    print(f"This means that your intelligence modifier is {intelligence_mod}.")
    input("Press ENTER to continue.")

    rolls = [random.randint(1, 6) for _ in range(4)]

    print(f"You rolled: {', '.join(map(str, rolls))}")

    wis = sum(rolls) - min(rolls)
    wis_mod = next(mod for rng, mod in modifiers.items() if wis in rng)

    time.sleep(1)

    print(f"Removing {min(rolls)} as it is the lowest roll.")
    time.sleep(1)
    print(f"Your wisdom score is {wis}.")
    time.sleep(1)
    print(f"This means that your wisdom modifier is {wis_mod}.")
    input("Press ENTER to continue.")

    rolls = [random.randint(1, 6) for _ in range(4)]

    print(f"You rolled: {', '.join(map(str, rolls))}")

    cha = sum(rolls) - min(rolls)
    cha_mod = next(mod for rng, mod in modifiers.items() if cha in rng)

    time.sleep(1)
    print(f"Removing {min(rolls)} as it is the lowest roll.")
    time.sleep(1)
    print(f"Your charisma score is {cha}.")
    time.sleep(1)
    print(f"This means that your charisma modifier is {cha_mod}.")
    input("Press ENTER to continue.")

    print(
        f"Your total ability scores:\nStrength: {strength} +{strength_mod}\nDexterity: {dex} +{dex_mod}\nConstitution: {con} +{con_mod}\nIntelligence: {intelligence} +{intelligence_mod}\nWisdom: {wis} +{wis_mod}\nCharisma: {cha} +{cha_mod}"
    )

    adventure()

def adventure():
    print(f"We are now ready to start the adventure, {full_name}!")

startup()