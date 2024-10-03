import json, random, main

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
    main.quest()

def innkeeper_shop():
    with open("stats.json", "r") as f:
        stats = json.load(f)

    print(f"{GREEN}GOLD:{RESET} {stats['gold']}\n ")
    
    for index, item in enumerate(innkeeper_items):
        print(f"[{index + 1}] {item} {innkeeper_items[item]} GP")
    
    while True:
        answer = int(input("> "))

        if answer == 1:
            if stats["gold"] < 5:
                print("You don't have enough gold to buy this item.")
                break
            
            else:
                innkeeper_items.remove("ale")
                stats["gold"] -= 5
                break
        
        elif answer == 2:
            if stats["gold"] < 10:
                print("You don't have enough gold ot buy this item.")
                break
            
            else:
                innkeeper_items.remove("grilled pork")
                stats["gold"] -= 10
                break
    
    with open("stats.json", "w") as f:
        json.dump(stats, f, indent = 4)

item_locations = {
    "innkeeper": innkeeper,
    "man": man,
    "man without innkeeper": man,
}

innkeeper_items = {
    "Ale": 5,
    "Grilled pork": 10,
}