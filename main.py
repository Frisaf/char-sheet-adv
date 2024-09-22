import random, time, json, attack, interact

YELLOW = "\033[33m"
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"
CYAN = "\033[36m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
PURPLE = "\033[35m"
INDENT = " "*20
BLUE = "\033[34m"

class Location:
    def __init__(self, name, description, directions):
        self.name = name
        self.description = description
        self.directions = directions

dir_aliases = {
    "right": ["r", "right", "east", "e"],
    "left": ["l", "left", "west", "w"],
    "forwards": ["f", "forwards", "north", "n"],
    "backwards": ["b", "backwards", "south", "s"]
}

def alt_directions(direction):
    for main_dir, aliases in dir_aliases.items():
        if direction in aliases:
            return main_dir
    return None

locations = {
    # THE INN
    "the inn": Location("the inn", "The inn smells of ale and food. The inn is fairly empty, which is understandable considering the time of the day, but the innkeeper is standing behind the counter to your left and there is a man sitting and eating some food in one corner, right in front of you.", {"left": "innkeeper", "forwards": "man"}),
    "the inn without innkeeper": Location("the inn", "The inn smells of ale and food. The inn is fairly empty, which is understandable considering the time of the day, but there is a man sitting and eating some food in one corner, right in front of you. The innkeeper lies dead behind the counter.", {"forwards": "man without innkeeper"}),
    "innkeeper": Location("the innkeeper", "The innkeeper looks at you.", {"backwards": "the inn",}),
    "man": Location("the man", "The man looks at you.", {"backwards": "the inn",}),
    "man without innkeeper": Location("the man", "The man looks at you.", {"backwards": "the inn without innkeeper"}),
    # QUEST
    "outside": Location("Berthold", "You follow Berthold outside. He explains that the evil wizard Magico plans to make the entire world's population to his slaves, and with that take over the world.\n'I need a brave adventurer like you to stop Magico's evil plans', Berthold says, 'you can kill him, or if you are able to take him here and let him serve his lifetime in jail. The choice is entirely up to you. Now, you might wonder where Magico lives, and the truth is that no one knows exactly where. There was a traveller who disappeared on a trip to the Great Canyon, which is to the west. I suggest you go there.'\n\nSAVEPOINT: You cannot go back to the inn", {"left": "canyon"}),
    "canyon": Location("the west, to the canyon", "You arrive to the Great Canyon, the place where Berthold said Magico probably lived. You walk along the edge of the canyon, searching for any signs of a hidden base somewhere.", {})
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
    
    def interact(self, item_name):
        item_locations = {
            "innkeeper": "innkeeper",
            "man": "man",
        }

        if item_name in item_locations:
            expected_location = locations[item_locations[item_name]]

            if self.current_location == expected_location:
                if item_name in interact.item_locations:
                    interact.item_locations[item_name]()

            else:
                print("You cannot do that...")
        
        else:
            print("You cannot interact with this.")
    
    def attack(self, npc):
        npc_locations = {
            "innkeeper": "innkeeper",
        }

        if npc in npc_locations:
            expected_location = locations[npc_locations[npc]]

            if self.current_location == expected_location:
                if npc in attack.npc_locations:
                    attack.npc_locations[npc]()
                
                else:
                    print("You cannot do that...")
            
            else:
                print("You cannot do that...")
        
        else:
            print("That is not a valid NPC to attack.")

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
    with open("stats.json", "r") as f:
        stats = json.load(f)

    while True:
        print("Welcome, adventurer! Let's start with making a character sheet.")
        name = input("What is your character's name? Type 'random' or 'ran' and press ENTER to get a random name.\n> ").lower()

        if name == "ran" or name == "random":
            global full_name

            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            stats["full_name"] = f"{first_name} {last_name}"
            full_name = stats["full_name"]

            print(f"Your character's name is {full_name}")
        
        else:
            stats["full_name"] = name.title()
            full_name = stats["full_name"]

            print(f"Your character's name is {full_name}")
        
        proceed_ans = input(f"Looks good, {full_name}? Type yes or no.\n> ").lower()

        if proceed_ans == "yes":
            with open("stats.json", "w") as f:
                json.dump(stats, f, indent = 4)

            set_scores()
            break
        
        elif proceed_ans == "no":
            continue
        else:
            print("Please answer yes or no.")

def set_scores():
    with open("stats.json", "r") as f:
        stats = json.load(f)

    print(f"Let's roll your ability scores!")
    input("Press ENTER to continue.")

    rolls = [random.randint(1, 6) for _ in range(4)]

    print(f"You rolled: {', '.join(map(str, rolls))}")

    stats["strength"] = sum(rolls) - min(rolls)
    strength = stats["strength"]
    stats["strength_mod"] = next(mod for rng, mod in modifiers.items() if strength in rng)
    strength_mod = stats["strength_mod"]

    time.sleep(1)

    print(f"Removing {min(rolls)} as it is the lowest roll.")
    time.sleep(1)
    print(f"Your strength score is {strength}.")
    time.sleep(1)
    print(f"This means that your strength modifier is {strength_mod}.")
    input("Press ENTER to continue.")

    rolls = [random.randint(1, 6) for _ in range(4)]

    print(f"You rolled: {', '.join(map(str, rolls))}")

    stats["dex"] = sum(rolls) - min(rolls)
    dex = stats["dex"]
    stats["dex_mod"] = next(mod for rng, mod in modifiers.items() if dex in rng)
    dex_mod = stats["dex_mod"]

    time.sleep(1)

    print(f"Removing {min(rolls)} as it is the lowest roll.")
    time.sleep(1)
    print(f"Your dexterity score is {dex}")
    time.sleep(1)
    print(f"This means that your dexterity modifier is {dex_mod}")
    input("Press ENTER to continue.")

    rolls = [random.randint(1, 6) for _ in range(4)]

    print(f"You rolled: {', '.join(map(str, rolls))}")

    stats["con"] = sum(rolls) - min(rolls)
    con = stats["con"]
    stats["con_mod"] = next(mod for rng, mod in modifiers.items() if con in rng)
    con_mod = stats["con_mod"]

    time.sleep(1)

    print(f"Removing {min(rolls)} as it is the lowest roll.")
    time.sleep(1)
    print(f"Your constitution score is {con}")
    time.sleep(1)
    print(f"This means that your constitution modifier is {con_mod}")
    input("Press ENTER to continue.")

    rolls = [random.randint(1, 6) for _ in range(4)]

    print(f"You rolled: {', '.join(map(str, rolls))}")

    stats["intelligence"] = sum(rolls) - min(rolls)
    intelligence = stats["intelligence"]
    stats["intelligence_mod"] = next(mod for rng, mod in modifiers.items() if intelligence in rng)
    intelligence_mod = stats["intelligence_mod"]

    time.sleep(1)
    
    print(f"Removing {min(rolls)} as it is the lowest roll.")
    time.sleep(1)
    print(f"Your intelligence score is {intelligence}.")
    time.sleep(1)
    print(f"This means that your intelligence modifier is {intelligence_mod}.")
    input("Press ENTER to continue.")

    rolls = [random.randint(1, 6) for _ in range(4)]

    print(f"You rolled: {', '.join(map(str, rolls))}")

    stats["wis"] = sum(rolls) - min(rolls)
    wis = stats["wis"]
    stats["wis_mod"] = next(mod for rng, mod in modifiers.items() if wis in rng)
    wis_mod = stats["wis_mod"]

    time.sleep(1)

    print(f"Removing {min(rolls)} as it is the lowest roll.")
    time.sleep(1)
    print(f"Your wisdom score is {wis}.")
    time.sleep(1)
    print(f"This means that your wisdom modifier is {wis_mod}.")
    input("Press ENTER to continue.")

    rolls = [random.randint(1, 6) for _ in range(4)]

    print(f"You rolled: {', '.join(map(str, rolls))}")

    stats["cha"] = sum(rolls) - min(rolls)
    cha = stats["cha"]
    stats["cha_mod"] = next(mod for rng, mod in modifiers.items() if cha in rng)
    cha_mod = stats["cha_mod"]

    time.sleep(1)
    print(f"Removing {min(rolls)} as it is the lowest roll.")
    time.sleep(1)
    print(f"Your charisma score is {cha}.")
    time.sleep(1)
    print(f"This means that your charisma modifier is {cha_mod}.")
    input("Press ENTER to continue.")

    global health_points
    global armour_class
    stats["health_points"] = random.randint(1, 20) + stats["con_mod"]
    health_points = stats["health_points"]
    stats["armour_class"] = dex_mod + 10
    armour_class = stats["armour_class"]

    with open("stats.json", "w") as f:
        json.dump(stats, f, indent = 4)

    print(f"Your total ability scores:\nStrength: {strength} +{strength_mod}\nDexterity: {dex} +{dex_mod}\nConstitution: {con} +{con_mod}\nIntelligence: {intelligence} +{intelligence_mod}\nWisdom: {wis} +{wis_mod}\nCharisma: {cha} +{cha_mod}\n\nHealth Points: {health_points}\nArmour Class: {armour_class}")
    print(f"We are now ready to start the adventure, {full_name}!")

    the_inn()

def the_inn():
    player = Player(locations["the inn"])
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

                if npc == "":
                    print("You need to specify what you want to attack.")
                
                else:
                    player.attack(npc)
            
            except IndexError:
                print(f"That is not a valid command. Did you perhaps have a typo?")

        else:
            print(f"You cannot do that...")

def the_inn_no_innkeeper():
    player = Player(locations["the inn without innkeeper"])
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

                if npc == "":
                    print("You need to specify what you want to attack.")
                
                else:
                    player.attack(npc)
            
            except IndexError:
                print(f"That is not a valid command. Did you perhaps have a typo?")

        else:
            print(f"You cannot do that...")

def quest():
    player = Player(locations["outside"])
    print("You are currently outside the inn.")

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

                if npc == "":
                    print("You need to specify what you want to attack.")
                
                else:
                    player.attack(npc)
            
            except IndexError:
                print(f"That is not a valid command. Did you perhaps have a typo?")

        else:
            print(f"You cannot do that...")

if __name__ == "__main__":
    startup()