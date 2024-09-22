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

with open("stats.json", "r") as f:
    stats = json.load(f)

def innkeeper():
    print(f"Hello there, {stats['full_name']}! I've heard a lot about you. They say you have done heroic things. Why don't you speak with Berthold, the man over there?\n{ITALIC}She points to the man in the corner{RESET}\nI think he really wants to speak with you.")

def man():
    print(f"Greetings, {stats['full_name']}. My name is Berthold. I've heard a lot about you. In fact, I am in dire need of your services.")

    answer = input("Do you think you can help? (Type yes or no)\n> ").lower()

    while True:
        if answer == "yes":
            break
        
        elif answer == "no":
            print("Really? That's a shame... What if I told you that the entire world might cease to exist would we not complete this mission?")
            print("Rolling insight (wisdom).\nYou need a 25 to succeed.")
            input("Press ENTER to continue.")

            insight_roll = random.randint(1, 20) + stats["wis_mod"]

            print(f"You rolled {insight_roll} +{stats['wis_mod']}")
            input("Press ENTER to continue")

            if insight_roll == 20 or insight_roll >=25:
                print("You listen carefully to the man's words, but the man speaks truth. The world is in danger and it needs your help.")
                print("You agree to the quest.")
                break

            elif insight_roll < 25:
                print("You don't sense any lie behind Berthold's words. The world is indeed in danger, and it needs your help.")
                print("You agree to the quest.")
                break
        
        else:
            print("You need to answer yes or no.")
    
    print("Awesome, follow me.")
    main.quest()

item_locations = {
    "innkeeper": innkeeper,
    "man": man,
}