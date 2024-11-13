import random, time, json, attack, interact

with open("stats.json", "r") as f:
    stats = json.load(f)

stats["lever broken"] = False
stats["investigated_traces"] = False

with open("npc_stats.json", "r") as f:
    npc_stats = json.load(f)

npc_stats["innkeeper alive"] = True

with open("npc_stats.json", "w") as f:
    json.dump(npc_stats, f, indent = 4)

with open("inventory.json", "r") as f:
    inventory = json.load(f)

inventory = {}

with open("inventory.json", "w") as f:
    json.dump(inventory, f, indent = 4)

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
WHITEB = "\033[47m"

class Location:
    def __init__(self, name, description, directions):
        self.name = name
        self.description = description
        self.directions = directions

dir_aliases = {
    "right": ["r", "right", "east", "e"],
    "left": ["l", "left", "west", "w"],
    "forwards": ["f", "forwards", "north", "n", "forward"],
    "backwards": ["b", "backwards", "south", "s", "backward"]
}

def alt_directions(direction):
    for main_dir, aliases in dir_aliases.items():
        if direction in aliases:
            return main_dir
    return None

locations = {
    # THE INN
    "the inn": Location("the inn", f"{YELLOW}The inn smells of ale and food. The inn is fairly empty, which is understandable considering the time of the day.{RESET}", {"left": "innkeeper", "forwards": "man"}),
    "innkeeper": Location("the innkeeper", f"{YELLOW}The innkeeper looks at you.{RESET}", {"backwards": "the inn",}),
    "man": Location("the man", f"{YELLOW}The man looks at you.{RESET}", {"backwards": "the inn",}),
    # QUEST
    "outside": Location("Berthold", f"{YELLOW}You follow Berthold outside. He explains that the evil wizard Magico plans to make the entire world's population to his slaves, and with that take over the world.\n{PURPLE}'I need a brave adventurer like you to stop Magico's evil plans'{YELLOW}, Berthold says,{PURPLE} 'you can kill him, or if you are able to take him here and let him serve his lifetime in jail. The choice is entirely up to you. Now, you might wonder where Magico lives, and the truth is that no one knows exactly where. There was a traveller who disappeared on a trip to the Great Canyon, which is to the west. I suggest you go there. Take this sword as well. You will definitely need it.'\n\n{RED}SAVEPOINT:{GREEN} You cannot go back to the inn\n{RED}SYSTEM: {GREEN}Short sword acquired{RESET}", {"left": "canyon"}),
    "canyon": Location("the west, to the canyon", f"{YELLOW}You arrive to the Great Canyon, the place where Berthold said Magico probably lived. You walk along the edge of the {CYAN}canyon{YELLOW}, searching for any signs of a hidden base somewhere.{RESET}", {}),
    "magico lair entrance": Location("the hole and jump down.", f"{YELLOW}The hole is tight, but you manage to squeeze through without any major injuries. It feels like you are crawling for forever, but suddenly you can see a little bit of light coming from a half opened hatch at the end of the tunnel.{RESET}", {"forwards": "the door room", "backwards": "canyon"}),
    "the door room": Location("the door room", f"{YELLOW}You open the hatch and fall down into a room with stone walls, stone floor and a ceiling, from where you came through the hatch, which seems to be made out of the same stone type as the canyon. There are two doors in the room, one to your right and one to your left, but something much bigger catches your eye: a big hole in the wall right in front of you.{RESET}", {"right": "right door room", "left": "left door room", "forwards": "hole in wall"}),
    "right door room": Location("to the right", f"{YELLOW}The room has the same type of walls, ceiling and floor as the last room had, but is much smaller. It is empty, save for a {CYAN}lever{YELLOW} on one of the walls.{RESET}", {"backwards": "the door room"}),
    "left door room": Location("to the left", f"{YELLOW}This room has the same type of walls, ceiling and floor as the last room had, but it is much smaller. In the middle of the room, there is a table with several millimeters of dust on. You would think that no one has been here for years, would it not be for the {CYAN}traces{YELLOW} in the dust. On top of the table, there is a {CYAN}letter{YELLOW}.{RESET}", {"backwards": "the door room"}),
    "hole in wall": Location("through the hole in the wall", f"{YELLOW}You enter a dark corridor. It seems to, just like the hole you entered through, be endless and pitch black. You continue to walk through the darkness until you suddenly feel a hand on your shoulder. You freeze turn around and see a pale, lifeless face stare right back at you.\n{PURPLE}'You shouldn't be here',{YELLOW} the person says with a monotone voice.{PURPLE} 'The master will be angry.'\n{YELLOW}The person takes a step back and draws their weapon, a rusty dagger.\n\n{RED}SYSTEM:{GREEN} Type 'attack person' to prepare yourself for an attack! You cannot go back from here...{RESET}", {}),
    # FINAL BATTLE
    "corridor": Location("to the corridor", f"{YELLOW}The corridor is pitch black and you can barely see a thing. The lifeless corpse of the {CYAN}person{YELLOW} you just killed lies in front of you.{RESET}", {"forwards": "blocked crossroad"}),
    "blocked crossroad": Location("forwards", f"{YELLOW}You continue to walk through the darkness, and you soon realise that the corridor has been blocked off by a bunch of big rocks.\n{PURPLE}'More humans?'{YELLOW} you hear a voice say from behind you. It comes from a man wearing a purple robe with a cone shaped hat in the same colour. An orb floating next to the man is radiating a bright light on you both. You realise that this must be Magico.\n{PURPLE} 'Seems like your friend has come to take you from me',{YELLOW} he says\nAt first, you are confused. What is he talking about? Then you see a shadow approaching from behind the man. It is a person, looking rather normal to be in an ancient wizard's lair, but you don't spot any life in their eyes. There is no emotion behind those eyes, no life, only darkness and a will to follow their master: Magico. This must be the enslaved adventurer Berthold was talking about.\n\n{RED}SYSTEM:{GREEN} You cannot go back from here", {}),
}

class Player:
    def __init__(self, current_location):
        self.current_location = current_location

    def move(self, direction):
        if direction in self.current_location.directions:
            next_location_name = self.current_location.directions[direction]
            next_location = locations[next_location_name]
            self.current_location = next_location
            print(f"{YELLOW}You walk to {BOLD}{BLUE}{next_location.name}{RESET}")
        else:
            print("You cannot go that way...")
    
    def interact(self, item_name):
        item_locations = {
            "innkeeper": "innkeeper",
            "man": "man",
            "canyon": "canyon",
            "hole": "canyon",
            "lever": "right door room",
            "traces": "left door room",
            "letter": "left door room",
            "magico": "blocked crossroad",
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
            "person": "hole in wall",
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
            print(f"The gods forbid you to attack {npc}: This is not a valid NPC to attack.")

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
    
    print(f"{RED}SYSTEM: {GREEN}Welcome to Escape 2: The Rescue, adventurer! Here are some useful tips that will help you progress the story.\n\nThere are seven different commands, four for movement, two for interacting with your environment and one to view your inventory:{RED}\n- {YELLOW}move{GREEN} forwards/left/right/backwards {RED}(move in the chosen direction)\n- {YELLOW}interact {GREEN}[item]{RED} (interact with something in the room)\n- {YELLOW}attack{GREEN} [NPC]{RED} (attack an npc) \n- {YELLOW}inv {RED}(view inventory)\nThere are aliases for these as well: {YELLOW}forward{GREEN} = f, north, n, forward {RED}| {YELLOW}left{GREEN} = l, west, w {RED}| {YELLOW}right{GREEN} = r, east, e {RED}| {YELLOW}backwards{GREEN} = b, south, s, backward {RED}| {YELLOW}interact {GREEN}= int {RED}| {YELLOW}attack {GREEN}= a\n\nItems that you can interact with are written in {CYAN}cyan{GREEN}. You can attempt to attack all NPC:s, but the gods will not always allow it...\n\nWith that out of the way, let's play the game!{RESET}")
    input("Press ENTER to continue")

    while True:
        print(f"{BOLD}{BLUE}Welcome, adventurer! Let's start with making a character sheet.{RESET}")
        name = input(f"{BLUE}What is your character's name? Type 'random' or 'ran' and press ENTER to get a random name.\n>{RESET} ").lower()

        if name == "ran" or name == "random":
            global full_name

            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            stats["full_name"] = f"{first_name} {last_name}"
            full_name = stats["full_name"]

            print(f"{RED}Your character's name is{BLUE} {full_name}{RESET}")
        
        else:
            stats["full_name"] = name.title()
            full_name = stats["full_name"]

            print(f"{RED}Your character's name is{BLUE} {full_name}{RESET}")
        
        proceed_ans = input(f"{BLUE}Looks good, {full_name}? Type yes or no.\n>{RESET} ").lower()

        if proceed_ans == "yes":
            with open("stats.json", "w") as f:
                json.dump(stats, f, indent = 4)

            set_scores()
            break
        
        elif proceed_ans == "no":
            continue
        else:
            print(f"{BLUE}Please answer yes or no.{RESET}")

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
    stats["health_points"] = random.randint(10, 20) + stats["con_mod"]
    health_points = stats["health_points"]
    stats["armour_class"] = dex_mod + 10
    armour_class = stats["armour_class"]
    stats["gold"] = random.randint(1, 4) * 10
    gold = stats["gold"]

    with open("stats.json", "w") as f:
        json.dump(stats, f, indent = 4)

    print(f"Your total ability scores:\nStrength: {strength} +{strength_mod}\nDexterity: {dex} +{dex_mod}\nConstitution: {con} +{con_mod}\nIntelligence: {intelligence} +{intelligence_mod}\nWisdom: {wis} +{wis_mod}\nCharisma: {cha} +{cha_mod}\n\nHealth Points: {health_points}\nArmour Class: {armour_class}\nGold: {gold}")
    print(f"We are now ready to start the adventure, {full_name}!")

    the_inn()

def the_inn():
    player = Player(locations["the inn"])
    print("Your are currently in the inn")

    while True:
        print(player.current_location.description)

        with open("npc_stats.json", "r") as f:
            npc_stats = json.load(f)
        
        if npc_stats["innkeeper alive"] == True and player.current_location.description == f"{YELLOW}The inn smells of ale and food. The inn is fairly empty, which is understandable considering the time of the day.{RESET}":
            print("The innkeeper is standing behind the counter to your left and there is a man sitting and eating some food in one corner, right in front of you.")
        
        elif npc_stats["innkeeper alive"] == False and player.current_location.description == f"{YELLOW}The inn smells of ale and food. The inn is fairly empty, which is understandable considering the time of the day.{RESET}":
            print("The innkeeper lies dead behind the counter, and your entire body is soaked in her blood. Right in front of you, there is a man sitting and eating some food in the corner of the inn.")

        command = input(f"What do you want to do? ").lower()

        if command.startswith("move") or command.startswith("m"):
            try:
                direction = command.split()[1]
                direction = alt_directions(direction)
                player.move(direction)

            except IndexError:
                print(f"That is not a valid command. Did you perhaps have a typo?")

        elif command.startswith("interact") or command.startswith("int"):
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
        
        elif command.startswith("inv"):
            with open("inventory.json", "r") as f:
                inventory = json.load(f)
            
            with open("stats.json", "r") as f:
                stats = json.load(f)

            print(f"{GREEN}Your inventory:\nGold:{RESET} {stats["gold"]}\n ")
        
            for index, item in enumerate(inventory):
                print(f"[{index + 1}] {item}")

            print("Type 'q' to exit inventory")

            inventory_list = list(inventory.keys())

            while True:
                answer = input("> ").lower()

                if answer == "q":
                    break

                elif 1 <= int(answer) <= len(inventory_list):
                    used_item = inventory_list[int(answer) - 1]
                    healing_value = inventory[used_item][0]

                    stats["health_points"] += healing_value

                    print(f"You used {used_item} and regained {healing_value} health points")

                    del inventory[used_item]
                    inventory_list.remove(used_item)

                    with open("stats.json", "w") as f:
                        json.dump(stats, f, indent = 4)
                    
                    with open("inventory.json", "w") as f:
                        json.dump(inventory, f, indent = 4)
                    
                    break

                else:
                    print("Please provide a valid answer.")

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

        elif command.startswith("interact") or command.startswith("int"):
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
        
        elif command.startswith("inv"):
            with open("inventory.json", "r") as f:
                inventory = json.load(f)
            
            with open("stats.json", "r") as f:
                stats = json.load(f)

            print(f"{GREEN}Your inventory:\nGold:{RESET} {stats["gold"]}\n ")
        
            for index, item in enumerate(inventory):
                print(f"[{index + 1}] {item}")

            print("Type 'q' to exit inventory")

            inventory_list = list(inventory.keys())

            while True:
                answer = input("> ").lower()

                if answer == "q":
                    break

                elif 1 <= int(answer) <= len(inventory_list):
                    used_item = inventory_list[int(answer) - 1]
                    healing_value = inventory[used_item][0]

                    stats["health_points"] += healing_value

                    print(f"You used {used_item} and regained {healing_value} health points")

                    del inventory[used_item]
                    inventory_list.remove(used_item)

                    with open("stats.json", "w") as f:
                        json.dump(stats, f, indent = 4)
                    
                    with open("inventory.json", "w") as f:
                        json.dump(inventory, f, indent = 4)
                    
                    break

                else:
                    print("Please provide a valid answer.")

        else:
            print(f"You cannot do that...")

def magico_lair():
    player = Player(locations["magico lair entrance"])
    print("You are currently standing in the canyon, gazing down in what seems like an endless tunnel.")

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

        elif command.startswith("interact") or command.startswith("int"):
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
        
        elif command.startswith("inv"):
            with open("inventory.json", "r") as f:
                inventory = json.load(f)
            
            with open("stats.json", "r") as f:
                stats = json.load(f)

            print(f"{GREEN}Your inventory:\nGold:{RESET} {stats["gold"]}\n ")
        
            for index, item in enumerate(inventory):
                print(f"[{index + 1}] {item}")

            print("Type 'q' to exit inventory")

            inventory_list = list(inventory.keys())

            while True:
                answer = input("> ").lower()

                if answer == "q":
                    break

                elif 1 <= int(answer) <= len(inventory_list):
                    used_item = inventory_list[int(answer) - 1]
                    healing_value = inventory[used_item][0]

                    stats["health_points"] += healing_value

                    print(f"You used {used_item} and regained {healing_value} health points")

                    del inventory[used_item]
                    inventory_list.remove(used_item)

                    with open("stats.json", "w") as f:
                        json.dump(stats, f, indent = 4)
                    
                    with open("inventory.json", "w") as f:
                        json.dump(inventory, f, indent = 4)
                    
                    break

                else:
                    print("Please provide a valid answer.")

        else:
            print(f"You cannot do that...")

def final_battle():
    player = Player(locations["corridor"])
    print("You are currently in the corridor.")

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

        elif command.startswith("interact") or command.startswith("int"):
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
        
        elif command.startswith("inv"):
            with open("inventory.json", "r") as f:
                inventory = json.load(f)
            
            with open("stats.json", "r") as f:
                stats = json.load(f)

            print(f"{GREEN}Your inventory:\nGold:{RESET} {stats["gold"]}\n ")
        
            for index, item in enumerate(inventory):
                print(f"[{index + 1}] {item}")

            print("Type 'q' to exit inventory")

            inventory_list = list(inventory.keys())

            while True:
                answer = input("> ").lower()

                if answer == "q":
                    break

                elif 1 <= int(answer) <= len(inventory_list):
                    used_item = inventory_list[int(answer) - 1]
                    healing_value = inventory[used_item][0]

                    stats["health_points"] += healing_value

                    print(f"You used {used_item} and regained {healing_value} health points")

                    del inventory[used_item]
                    inventory_list.remove(used_item)

                    with open("stats.json", "w") as f:
                        json.dump(stats, f, indent = 4)
                    
                    with open("inventory.json", "w") as f:
                        json.dump(inventory, f, indent = 4)
                    
                    break

                else:
                    print("Please provide a valid answer.")

        else:
            print(f"You cannot do that...")

if __name__ == "__main__":
    startup()