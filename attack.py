import random, json
from main import startup, the_inn, magico_lair, final_battle

with open("stats.json", "r") as f:
    stats = json.load(f)

with open("npc_stats.json", "r") as f:
    npc_stats = json.load(f)

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

weapon = stats["weapon"]
strength = stats["strength"]
strength_mod = stats["strength_mod"]
dex = stats["dex"]
dex_mod = stats["dex_mod"]
con = stats["con"]
con_mod = stats["con_mod"]
intelligence = stats["intelligence"]
intelligence_mod = stats["intelligence_mod"]
wis = stats["wis"]
wis_mod = stats["wis_mod"]
cha = stats["cha"]
cha_mod = stats["cha_mod"]
health_points = stats["health_points"]
armour_class = stats["armour_class"]

weapons = {
    "shortsword": 6
}

def innkeeper():
    with open("stats.json", "r") as f:
        stats = json.load(f)

    with open("npc_stats.json", "r") as f:
        npc_stats = json.load(f)
        
    npc_hp = 10

    while npc_hp > 0:
        hit_roll = random.randint(1, 20)
        
        if weapon == "":
            weapon_damage = random.randint(1, 20) + strength_mod

        else:
            weapon_damage = random.randint(1, weapons[weapon])

        if hit_roll >= 10:
            print(f"You rolled {hit_roll} and land a hit on the innkeeper.")
            npc_hp -= weapon_damage
            print(f"You deal {weapon_damage} damage")
            print("It is now the innkeeper's turn")
            input("Press ENTER to continue.")
        
        else:
            print(f"You rolled a {hit_roll} and don't hit! It's the innkeeper's turn.")
            input("Press ENTER to continue.")

        npc_hit = random.randint(1, 20)

        if npc_hit >= armour_class:
            npc_attack_roll = random.randint(1, 6)
            stats["health_points"] -= npc_attack_roll

            with open("stats.json", "w") as f:
                json.dump(stats, f, indent = 4)

            print(f"The innkeeper lands a hit and deals {npc_attack_roll} damage!")
            print(f"You currently have {stats['health_points']} HP")
        
        else:
            print("The innkeeper did not hit! It is now your turn.")
        
        if stats["health_points"] <= 0:
            print("You died!")
            
            while True:
                answer = input("Do you want to restart the entire game, or do you want to restart from the latest checkpoint? Type 'RES' to restart the entire game with a new character, or type 'CHECK' to restart from the latest checkpoint.\n> ").upper()
                if answer == "RES":
                    startup()
                
                elif answer == "CHECK":
                    the_inn()
                
                else:
                    print("That is not a valid answer.")
        
        else:
            continue

    print("You killed the innkeeper!")

    npc_stats["innkeeper alive"] = False

    with open("npc_stats.json", "w") as f:
        json.dump(npc_stats, f, indent = 4)

    the_inn()

def person():
    with open("stats.json", "r") as f:
        stats = json.load(f)

    with open("npc_stats.json", "r") as f:
        npc_stats = json.load(f)
    
    if weapon == "":
        weapon_damage = random.randint(1, 20) + strength_mod

    else:
        weapon_damage = random.randint(1, weapons[weapon])

    npc_hp = 15

    while npc_hp > 0:
        print(f"{RED}SYSTEM:{GREEN} Rolling with disadvantage due to the darkness.")

        rolls = [random.randint(1, 20) for _ in range(2)]
        hit_roll = min(rolls)

        if hit_roll >= 7:
            print(f"You rolled {', '.join(map(str, rolls))}. Taking {min(rolls)} as it is the lowest value. You land a hit on your enemy.")
            npc_hp -= weapon_damage
            print(f"You deal {weapon_damage} damage")
            print("It is now your opponent's turn")
            input(f"{RESET}Press ENTER to continue.{GREEN}")
        
        else:
            print(f"You rolled {', '.join(map(str, rolls))}. Taking {min(rolls)} as it is the lowest value. You don't hit! It's your opponent's turn.")
            input(f"{RESET}Press ENTER to continue.{GREEN}")
        
        npc_hit = random.randint(1, 20)

        if npc_hit >= armour_class:
            npc_attack_roll = random.randint(1, 4)
            stats["health_points"] -= npc_attack_roll

            with open("stats.json", "w") as f:
                json.dump(stats, f, indent = 4)

            print(f"The person lands a hit and deals {npc_attack_roll} damage.")
            print(f"You currently have {stats['health_points']} HP")
        
        else:
            print("The other person did not hit! It is now your turn.")
        
        if stats["health_points"] <= 0:
            print(f"{RED}YOU DIED!{RESET}")
            
            while True:
                answer = input("Do you want to restart the entire game, or do you want to restart from the latest checkpoint? Type 'RES' to restart the entire game with a new character, or type 'CHECK' to restart from the latest checkpoint.\n> ").upper()
                if answer == "RES":
                    startup()
                
                elif answer == "CHECK":
                    magico_lair()
                
                else:
                    print("That is not a valid answer.")
        
        else:
            continue
    
    print("You killed the person")

    npc_stats["person alive"] = False

    with open("npc_stats.json", "w") as f:
        json.dump(npc_stats, f, indent = 4)

    final_battle()

def magico_battle():
    with open("stats.json", "r") as f:
        stats = json.load(f)

    with open("npc_stats.json", "r") as f:
        npc_stats = json.load(f)
    
    if weapon == "":
        weapon_damage = random.randint(1, 20) + strength_mod

    else:
        weapon_damage = random.randint(1, weapons[weapon])

    magico_hp = 30
    slave_hp = 15
    spell_broken = False
    missed = False

    print(f"{RED}SYSTEM:{GREEN} Magico sends his slave to attack first! Watch your step!")

    slave_options = [
        f"{ITALIC}Try to break the spell",
        f"{ITALIC}Attack",
    ]

    while spell_broken == False:
        for index, option in enumerate(slave_options):
            print(f"[{index + 1}] {option}")
        
        answer = int(input(f"{RESET}> "))

        try:
            if 1 <= answer <= len(slave_options):
                choice = slave_options[answer - 1]

                if choice == f"{ITALIC}Try to break the spell":
                    print(f"{YELLOW}You throw a rock at Magico to try to break his concentration. Rolling a dexterity check.")

                    dexterity_check = random.randint(1, 20)
                    magico_con_save = random.randint(1, 20)

                    if dexterity_check + stats[dex_mod] > magico_con_save:
                        print(f"{YELLOW}You throw a rock at Magico and he staggers back. The slave in front of you collapses to the floor, now unconscious.")
                        spell_broken = False
                    
                    else:
                        print(f"{YELLOW}You miss, and it is now the slave's turn to attack.")
                        missed = True
                        spell_broken == True
            
                elif choice == f"{ITALIC}Attack":
                    spell_broken == True

                else:
                    print("Please provide a valid answer.")
            
            else:
                print("Please provide a valid answer.")
        
        except ValueError:
            print("Please provide a valid answer.")

    if missed == True:
        print("It is the slave's turn to attack!")

        slave_attack_roll = random.randint(1, 20)

        if slave_attack_roll >= stats["armour_class"]:
            slave_damage_roll = random.randint(1, 10)
            stats["health_points"] -= slave_damage_roll
            print(f"The slave hit you and dealt {slave_damage_roll} damage. You currently have {stats['health_points']} HP.")
    
    while slave_hp > 0:
        print("It is your turn to attack!")

        attack_roll = random.randint(1, 20)

        if attack_roll >= 13:
            damage_roll = weapon_damage # HAS TO BE CHANGED LATER FOR IT TO BE RANDOM
            slave_hp -= damage_roll

            print(f"You hit and deal {damage_roll} damage to the slave.")
            print("It is now the slave's turn to attack.")

        else:
            print("You missed! This means that it is the slave's turn to attack.")

        slave_attack_roll = random.randint(1, 20)

        if slave_attack_roll >= stats["armour_class"]:
            slave_damage_roll = random.randint(1, 10)
            stats["health_points"] -= slave_damage_roll
            print(f"The slave hit you and dealt {slave_damage_roll} damage. You currently have {stats['health_points']} HP.")

npc_locations = {
    "innkeeper": innkeeper,
    "person": person
}