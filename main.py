import random, set_stats

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

def startup():
    print("Welcome, adventurer! Let's start with making a character sheet.")
    name = input("What is your character's name? Type 'ran' to get a random name.\n> ").lower()

    if name == "ran":
        global full_name

        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        full_name = f"{first_name} {last_name}"

        print(f"Your character's name is {full_name}")

    while True:
        proceed_ans = input(f"Looks good, {full_name}? Type yes or no.\n> ").lower()

        if proceed_ans == "yes":
            set_stats.set_scores()
            break
        
        elif proceed_ans == "no":
            startup()
            break
        
        else:
            print("Please answer yes or no.")

startup()