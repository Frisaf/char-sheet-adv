import json, random, main, attack

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

def innkeeper():
    with open("stats.json", "r") as f:
        stats = json.load(f)

    print(f"Hello there, {stats['full_name']}! I've heard a lot about you. They say you have done heroic things. Why don't you speak with Berthold, the man over there?\n{ITALIC}She points to the man in the corner{RESET}\nI think he really wants to speak with you.")
    print(f"[1] What do you sell?\n[2] How is business?\n[3] {ITALIC}Leave{RESET}")

    dialogue_answer = int(input("> "))

    while True:
        try:
            if dialogue_answer == 1:
                print("I sell lots of different things. Take a look.")
                innkeeper_shop()
                break
                
            
            elif dialogue_answer == 2:
                print("Well, people come in, they get drunk and they leave. That's how it goes every night. One get pretty tired of it eventually, but a poor widow has to earn her keep somehow.")
                break
            
            elif dialogue_answer == 3:
                print("Goodbye! See you later.")
                break 
            
            else:
                print("Please provide a valid answer")
        
        except ValueError:
            print("Please provide a valid answer")

def man():
    with open("stats.json", "r") as f:
        stats = json.load(f)

    print(f"Greetings, {stats['full_name']}. My name is Berthold. I've heard a lot about you. In fact, I am in dire need of your services. Do you think you can help?")
    print("[1] Yes, I'd love to. What do you need help with?\n[2] No, I don't want to help you.\n[3] Wait a moment")

    answer = int(input("> "))

    while True:
        try:
            if answer == 1:
                break
            
            elif answer == 2:
                print("Really? That's a shame... What if I told you that the entire world might cease to exist would we not complete this mission?")
                print("Rolling insight (wisdom).\nYou need a 25 to succeed.")
                input("Press ENTER to continue.")

                insight_roll = random.randint(1, 20)
                modifier = stats["wis_mod"]
                result = insight_roll + modifier

                print(f"You rolled {insight_roll} + {modifier}")
                input("Press ENTER to continue")

                if result == 20 or result >=25:
                    print("You listen carefully to the man's words, but the man speaks truth. The world is in danger and it needs your help.")
                    print("You agree to the quest.")
                    break

                elif result < 25:
                    print("You don't sense any lie behind Berthold's words. The world is indeed in danger, and it needs your help.")
                    print("You agree to the quest.")
                    break
            
            elif answer == 3:
                main.the_inn()
                break
            
            else:
                print("Please provide a valid answer")
        
        except ValueError:
            print("Please provide a valid answer")
    
    print("Awesome, follow me.")

    stats["weapon"] = "shortsword"
    main.quest()

def canyon():
    with open("stats.json", "r") as f:
        stats = json.load(f)

    print("Rolling a perception check. You need a 12 to succeed.")
    input("Press ENTER to continue")

    perception_roll = random.randint(1, 20) + stats["wis_mod"]

    if perception_roll >= 12:
        print(f"{GREEN}You rolled {perception_roll} and succeed.\n{YELLOW}You look around the canyon in search for something out of the ordinary. You see a small {CYAN}hole{YELLOW} behind a few rocks.")
    
    else:
        print(f"{GREEN}You rolled a {perception_roll} and don't succeed.\n{YELLOW}You look around the canyon in search for something out of the ordinary, but you can't find anything particularly interesting.")

def canyon_hole():
    with open("stats.json", "r") as f:
        stats = json.load(f)

    print(f"{YELLOW}The hole is tight and so deep that you cannot see to the bottom of it.")

    hole_options = [
        "Squeeze through and hope for the best",
        "Investigate the hole and try to look for where it might lead",
        f"{ITALIC}Leave{RESET}"
    ]

    while True:
        for index, item in enumerate(hole_options):
            print(f"{RED}[{index + 1}]{RESET} {item}")

        answer = int(input("> "))

        try:
            if 1 <= answer <= len(hole_options):
                choice = hole_options[answer - 1]

                if choice == "Squeeze through and hope for the best":
                    main.magico_lair()
                    break

                elif choice == "Investigate the hole and try to look for where it might lead":
                    print("Rolling an investigation check. You need a 10 to succeed.")

                    investigation_roll = random.randint(1, 20) + stats["intelligence_mod"]

                    print(f"{GREEN}You rolled {investigation_roll}{RESET}")

                    if investigation_roll >= 10:
                        print("You squint your eyes and focus on the darkness. You understand that the tight hole leads several meters down in the ground. Then it turns, so you don't see what's at the end of it.")
                    
                    else:
                        print("You squint your eyes and focus on the darkness, but you don't manage to see anything beyond a few meters. The only thing you know is that the hole is tight, and that you might have a hard time to fit through it.")
                    
                    hole_options.pop(1)
                
                elif choice == f"{ITALIC}Leave{RESET}":
                    break
        
        except ValueError:
            print("Please provide a valid answer.")

def lever():
    with open("stats.json", "r") as f:
        stats = json.load(f)
    
    with open("inventory.json", "r") as f:
        inventory = json.load(f)
    
    if stats["lever_broken"] == True:
        print("The broken lever is unusable.")
        return

    print(f"{YELLOW}You try to pull the lever, but it won't budge.\n{RED}[1]{RESET} [STRENGTH] Lay all your bodyweight onto the lever to try to push it downwards.\n{RED}[2]{RESET}{ITALIC}Leave{RESET}")

    while True:
        answer = int(input("> "))

        if answer == 1:
            print("Rolling strength. You need a 5 to succeed.")

            strength_roll = random.randint(1, 20) + stats["strength_mod"]

            if strength_roll >= 5:
                print(f"{YELLOW}You pull with all your power and hear a sudden click from the lever, but nothing happens. Instead, you have the broken lever in your hands.")

                inventory["broken_lever"] = ""

                with open("inventory.json", "w") as f:
                    json.dump(inventory, f, indent = 4)
                
                print(f"{RED}SYSTEM:{GREEN} Added {ITALIC}broken lever{RESET}{GREEN} to inventory.{RESET}")

                stats["lever_broken"] = True

                with open("stats.json", "w") as f:
                    json.dump(stats, f, indent = 4)

                break
            
            else:
                print("You try to pull the lever again with all your strength, but it still won't budge.")
                break

def traces():
    with open("stats.json", "r") as f:
        stats = json.load(f)

    if stats["investigated_traces"] == True:
        print(f"{RED}SYSTEM:{GREEN} You can't investigate this item twice.")
    
    else:
        print("Rolling an investigation check. You need a 7 to succeed.")

        investigation_roll = random.randint(1, 20) + stats["intelligence_mod"]

        if investigation_roll >= 7 or investigation_roll == 20:
            print(f"{RED}SYSTEM:{GREEN} You rolled a {investigation_roll} and succeed.\n{YELLOW}You notice that the traces are pretty fresh, as if someone has been there just recently.")
        
        else:
            print(f"{RED}SYSTEM:{GREEN} You rolled a {investigation_roll} and don't succeed.\n{YELLOW}You don't notice anything particularly interesting with the traces.")
        
        stats["investigated_traces"] = True

def letter():
    print(f"{YELLOW}You pick up the letter and read:\n{BOLD}{ITALIC}{PURPLE}It's been days, no weeks, since I last slept. If you read this, you need to leave now. This place is driving me insane. I haven't figured out the way out yet, but I think it has something to do with the lever in the other room...{RESET}")

def person():
    with open("stats.json", "r") as f:
        stats = json.load(f)

    print(f"{YELLOW}The person doesn't have a lot on them other than the rusty dagger they wielded in the battle against you.{RESET}\n[1] {ITALIC}Take the dagger{RESET}\n[2] {ITALIC}Leave")

    while True:
        answer = int(input("> "))

        if answer not in [1, 2]:
            print("Please provide a valid answer.")
        
        else:
            print(f"{YELLOW}You take the dagger. It feels light in your hand.\n{RED}SYSTEM:{GREEN} You already have a weapon! Do you want to replace your {stats['weapon']} with the {ITALIC}rusty dagger?{RESET}")

            choice = input("Yes or no: ").lower()

            if choice == "yes":
                stats["weapon"] = "rusty dagger"
                print(f"{RED}SYSTEM:{GREEN} Picked up and equipped {ITALIC}rusty dagger{RESET}{GREEN}. Dropped shortsword.")
                break
            
            elif choice == "no":
                print(f"{YELLOW}You drop the rusty dagger to the ground. It is to no use for you.")
                break
            
            else:
                print("Please provide a valid answer.")

def magico():
    with open("stats.json", "r") as f:
        stats = json.load(f)
    
    magico_options = [
        "Cancel the spell immediately, Magico, and you will walk out of here alive.",
        "What is this place...?",
        "This ends now! Die!",
    ]

    while True:
        for index, option in magico_options:
            print(f"[{index + 1}] {option}")
        
        answer = int(input("> "))

        if 1 <= answer <= len(magico_options):
            choice = magico_options[answer - 1]

            if choice == "Cancel the spell immediately, Magico, and you will walk out of here alive.":
                print(f"{YELLOW}Magico scoffs.\n{PURPLE}'You think you can kill me?'{YELLOW} he says,{PURPLE}'I have been master over this place for three hundered years! I am immortal, unlike you.'\n{YELLOW}He spits on the stone floor.\n{PURPLE}'The only one walking out of here alive is me.'{RESET}")

                attack.magico_battle()
            
            elif choice == "What is this place...?":
                print(f"{YELLOW}The light from the orb illuminates Magico's malicious grin.\n{PURPLE}'This, my dear soon-to-be-slave, is my lair, my base, my home, my lab, whatever you'd like to call it. One might think, how can someone live in this place? I asked myself the same question when I came here, but I found it to be a very good place to hide while I was building my army of lost adventurers.'{RESET}")

                magico_options.pop(1)
            
            elif choice == "This ends now! Die!":
                print(f"{PURPLE}'You will regret this choice, young adventurer',{YELLOW} Magico hisses, {PURPLE}'Slave 752, attack!'")

                attack.magico_battle()

def innkeeper_shop():
    innkeeper_items_list = list(innkeeper_items.keys())
    
    while True:
        with open("stats.json", "r") as f:
            stats = json.load(f)
    
        with open("inventory.json", "r") as f:
            inventory = json.load(f)

        print(f"{GREEN}GOLD:{RESET} {stats['gold']}\n ")

        if not innkeeper_items:
            print("Shop is empty")
            break
        
        else:
            for index, item in enumerate(innkeeper_items):
                print(f"[{index + 1}] {item} {innkeeper_items[item]} GP")
        
        print("Type 'q' to exit buy mode.")

        answer = input("> ").lower()

        if answer == "q":
            break

        elif 1 <= int(answer) <= len(innkeeper_items_list):
            bought_item = innkeeper_items_list[int(answer) - 1]
            price = innkeeper_items[bought_item]

            if stats["gold"] >= price:
                stats["gold"] -= price

                del innkeeper_items[bought_item]
                innkeeper_items_list.remove(bought_item)

                for characteristic in item_characteristics:
                    inventory[bought_item] = [item_characteristics[characteristic]]

                print(f"You bought {bought_item.lower()} for {price} GP")

                with open("stats.json", "w") as f:
                    json.dump(stats, f, indent = 4)
                
                with open("inventory.json", "w") as f:
                    json.dump(inventory, f, indent = 4)
            
            else:
                print("You don't have enough gold to buy that.")
    
        else:
            print("Please enter a valid answer")

item_locations = {
    "innkeeper": innkeeper,
    "man": man,
    "canyon": canyon,
    "hole": canyon_hole,
    "lever": lever,
    "traces": traces,
    "letter": letter,
    "magico": magico,
}

# item name - price
innkeeper_items = {
    "Ale": 5,
    "Grilled pork": 10,
}

# item name - amount of HP healed (for food)
item_characteristics = {
    "Ale": random.randint(1, 4),
    "Grilled pork": random.randint(1, 8),
}