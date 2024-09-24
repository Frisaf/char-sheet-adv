import random, json, main
from main import startup, the_inn, the_inn_no_innkeeper

with open("stats.json", "r") as f:
    stats = json.load(f)

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

unarmed_strike = random.randint(1, 20) + strength_mod

weapons = {
    "shortsword": random.randint(1, 6)
}

if weapon == "":
    weapon = unarmed_strike
    weapon_damage = 1 + strength_mod

else:
    weapon_damage = weapons[weapon]

def innkeeper():
    npc_hp = 10

    while npc_hp > 0:
        hit_roll = random.randint(1, 20)

        if hit_roll >= 10:
            print(f"You rolled {hit_roll} and land a hit on the innkeeper.")
            npc_hp -= weapon_damage
            print(f"You deal {weapon_damage} damage")
            print("It is now the innkeeper's turn")
            input("Press ENTER to continue.")
        
        else:
            print(f"You rolled a {hit_roll} and don't hit! It's the innkeeper's turn.")
            input("Press ENTER to continue.")

        npc_attack = random.randint(1, 6)

        if npc_attack >= armour_class:
            npc_hit_roll = random.randint(1, 20)
            stats["health_points"] -= npc_hit_roll

            with open("stats.json", "w") as f:
                json.dump(stats, f, indent = 4)

            print(f"The innkeeper lands a hit! and deals {npc_hit_roll} damage.")
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
    the_inn_no_innkeeper()

npc_locations = {
    "innkeeper": innkeeper,
}