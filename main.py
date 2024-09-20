import random, time, attack

weapon = False

class Location:
    def __init__(self, name, description, directions):
        self.name = name
        self.description = description
        self.directions = directions

dir_aliases = {
    "right": ["r", "right"],
    "left": ["l", "left"],
    "forwards": ["f", "forwards"],
    "backwards": ["b", "backwards"]
}

def alt_directions(direction):
    for main_dir, aliases in dir_aliases.items():
        if direction in aliases:
            return main_dir
    return None

locations = {
    # THE INN
    "the inn": Location("the inn", "The inn smells of ale and food. The inn is fairly empty, which is understandable considering the time of the day, but the innkeeper is standing behind the counter to your left and there is a man sitting and eating some food in one corner, right in front of you.", {"left": "innkeeper", "forwards": "man"}),
    "innkeeper": Location("the innkeeper", "The innkeeper looks at you.", {"backwards": "the inn",}),
    "man": Location("the man", "The man looks at you.", {"backwards": "the inn",})
}

class Player:
    def __init__(self, current_location):
        self.current_location = current_location

    def move(self, direction):
        if direction in self.current_location.directions:
            next_location_name = self.current_location.directions[direction]
            next_location = locations[next_location_name]
            self.current_location = next_location
            print(f"You walk to {next_location.name}")
        else:
            print("You cannot go that way...")
    
    # def interact(self, item_name):
        # interact logic
    
    def attack(self, npc):
        if npc == "innkeeper":
            if self.current_location == "innkeeper":
                attack.innkeeper()
            
            else:
                print("You cannot do that...")
        
        elif npc == "man":
            if self.current_location == "man":
                attack.man()
            
            else:
                print("You cannot do that...")

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
            full_name = name.capitalize()
            print(f"Your character's name is {full_name}")
        
        proceed_ans = input(f"Looks good, {full_name}? Type yes or no.\n> ").lower()

        if proceed_ans == "yes":
            set_scores()
            break
        
        elif proceed_ans == "no":
            continue
        else:
            print("Please answer yes or no.")

def set_scores():
    global strength
    global strength_mod
    global dex
    global dex_mod
    global con
    global con_mod
    global intelligence
    global intelligence_mod
    global wis
    global wis_mod
    global cha
    global cha_mod

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

    global health_points
    health_points = random.randint(1, 20) + con_mod

    print(f"Your total ability scores:\nStrength: {strength} +{strength_mod}\nDexterity: {dex} +{dex_mod}\nConstitution: {con} +{con_mod}\nIntelligence: {intelligence} +{intelligence_mod}\nWisdom: {wis} +{wis_mod}\nCharisma: {cha} +{cha_mod}\n\nHealth Points: {health_points}")

    the_inn()

def the_inn():
    player = Player(locations["the inn"])
    print(f"We are now ready to start the adventure, {full_name}!")
    print("Your are currently in the inn")

    while True:
        print(player.current_location.description)
        command = input(f"What do you want to do? ").lower()

        if command.startswith("move") or command.startswith("m"):
            try:
                direction = command.split()[1]
                direction = alt_directions(direction)
                player.move(direction)

            except IndexError:
                print(f"That is not a valid command. Did you perhaps have a typo?")

        elif command.startswith("interact") or command.startswith("i"):
            try:
                item = command.split()[1]
                player.interact(item)
            except IndexError:
                print(f"That is not a valid command. Did you perhaps have a typo?")
        
        elif command.startswith("attack") or command.startswith("a"):
            try:
                npc = command.split()[1]
                player.attack(npc)
            
            except IndexError:
                print(f"That is not a valid command. Did you perhaps have a typo?")

        else:
            print(f"You cannot do that...")

startup()