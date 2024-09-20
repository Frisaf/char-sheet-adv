import random, json

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

if weapon == "":
    weapon = unarmed_strike
    damage_unarmed = 1 + strength_mod

else:
    weapon = weapon

def innkeeper():
    npc_hp = 10
    damage_roll = damage_unarmed
    print(npc_hp)

    while npc_hp > 0:
        hit_roll = random.randint(1, 20)

        if hit_roll >= 10:
            print(f"You rolled {hit_roll} and land a hit on the innkeeper.")
            npc_hp -= damage_roll
            print(npc_hp)
        
        else:
            print("You don't hit! It's the innkeeper's turn.")
            npc_attack = random.randint(1, 20)

            if npc_attack >= armour_class:
                npc_hit_roll = random.randint(1, 20)
                stats[health_points] - npc_hit_roll

                with open("stats.json", "w") as f:
                    json.dump(stats, f, indent = 4)

                print("The innkeeper lands a hit!")
                print(f"You currently have {health_points}")

def man():
    print("You attack the man :3")

npc_locations = {
    "innkeeper": innkeeper,
    "man": man,
}