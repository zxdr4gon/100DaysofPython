import os
import time
import datetime
import random
import pyjokes

def clear():
    os.system('cls')

def intro():
    print("──────────────────────────────────────────────")
    print("\n   ☕  Welcome to the Coffee Machine  ☕\n")
    print("──────────────────────────────────────────────\n")

water = 300
milk = 200
coffee = 100
money = 0.0

recipes = {
    'espresso': {'water': 50, 'milk': 0, 'coffee': 18, 'cost': 1.5},
    'latte': {'water': 200, 'milk': 150, 'coffee': 24, 'cost': 2.5},
    'cappuccino': {'water': 250, 'milk': 100, 'coffee': 24, 'cost': 3.0}
}


def report(water, milk, coffee, money):
    print(f'''
📊 Current Resources:
💧 Water:  {water}ml
🥛 Milk:   {milk}ml
☕ Coffee: {coffee}g
💰 Money:  ${money:.2f}
''')


def check_resources(choice, water, milk, coffee):
    rec = recipes.get(choice)
    if not rec:
        return "Invalid selection.", False
    missing = []
    if rec['water'] > water:
        missing.append('water')
    if rec['milk'] > milk:
        missing.append('milk')
    if rec['coffee'] > coffee:
        missing.append('coffee')
    if missing:
        return f"Sorry, not enough {', '.join(missing)}.", False
    return "Resources sufficient.", True


def process_coins(cost):
    print(f"Please insert coins. Cost: ${cost:.2f}")
    try:
        quarters = int(input("How many quarters? "))   # $0.25
        dimes = int(input("How many dimes? "))         # $0.10
        nickels = int(input("How many nickels? "))     # $0.05
        pennies = int(input("How many pennies? "))     # $0.01
    except ValueError:
        print("Invalid input. Transaction cancelled.")
        return 0.0
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total


def make_coffee(choice):
    global water, milk, coffee, money
    rec = recipes[choice]
    water -= rec['water']
    milk -= rec['milk']
    coffee -= rec['coffee']
    money += rec['cost']
    
    # record order history
    if not hasattr(coffee_machine, "orders"):
        coffee_machine.orders = []
    coffee_machine.orders.append(choice)
    
    print(f"Here is your {choice}. Enjoy!")



def coffee_machine():
    global water, milk, coffee, money
    
    if not hasattr(coffee_machine, "orders"):
        coffee_machine.orders = []

    intro()
    print("Explore our menu to begin, or help to get help (type 'menu' or 'help')")


    while True:
        choice = input("\n➤  ").lower()
        print()
        
        if choice == "off":
            print("Turning off. Goodbye!")
            break
        
        elif choice == "report":
            report(water, milk, coffee, money)
        
        elif choice in recipes:
            msg, ok = check_resources(choice, water, milk, coffee)
            if not ok:
                print(msg)
                continue
            payment = process_coins(recipes[choice]['cost'])
            if payment < recipes[choice]['cost']:
                print("Sorry, that's not enough money. Money refunded.")
                continue
            change = payment - recipes[choice]['cost']
            if change > 0:
                print(f"Here is ${change:.2f} in change.")
            make_coffee(choice)

        elif choice == "cls":
            input("Press Enter to clear screen")
            clear()
            print("Screen cleared.")
            time.sleep(0.667)
            clear()
            intro()

        elif choice == "menu":
            print("━━━━━━ Menu ━━━━━━\n")
            for drink, rec in recipes.items():
                print(f"{drink.title()}: ${rec['cost']:.2f}")

        elif choice == "status":
            print("Current resource status:")
            report(water, milk, coffee, money)

        elif choice == "history":
            if not hasattr(coffee_machine, "orders") or not coffee_machine.orders:
                print("No orders yet.")
            else:
                print("Order history:")
                for idx, order in enumerate(coffee_machine.orders, 1):
                    print(f"{idx}. {order.title()}")

        elif choice == "reset":
            confirm = input("Are you sure you want to reset all resources and money? (yes/no): ").lower()
            if confirm == "yes":
                water = 300
                milk = 200
                coffee = 100
                money = 0.0
                if hasattr(coffee_machine, "orders"):
                    coffee_machine.orders.clear()
                print("Machine reset to default state.")

        elif choice == "admin":
            password = input("Enter admin password: ")
            if password == "admin123":
                print("Admin mode. Type 'refill' to restock resources or 'exit' to leave admin mode.")
                while True:
                    admin_cmd = input("admin> ").lower()
                    if admin_cmd == "refill":
                        water = 300
                        milk = 200
                        coffee = 100
                        print("Resources refilled.")
                    elif admin_cmd == "report":
                        report(water, milk, coffee, money)
                    elif admin_cmd == "srefill":
                        water = 1000
                        milk = 1000
                        coffee = 1000
                        print("Resources \"super\" refilled.")
                    elif admin_cmd == "exit":
                        print("Exiting admin mode.")
                        break
                    else:
                        print("Unknown admin command.")
            else:
                print("Incorrect password.")
        
        elif choice == "joke":
            try:
                print(pyjokes.get_joke())
            except ImportError:
                print("PyJokes not installed. Run 'pip install pyjokes' to enable jokes.")

        elif choice == "secret":
            print("🤫 You found the hidden easter egg!\nHere's a virtual cookie 🍪 and a free refill ☕")

        elif choice == "time":
            now = datetime.datetime.now()
            current_time = now.strftime("%I:%M:%S %p")      # Time on top
            current_date = now.strftime("%A, %B %d, %Y")    # Date on bottom
            print(f"⏰ Current time: {current_time}\n📅 Current date: {current_date}")

        elif choice == "tip":
            tips = [
                "Pro tip: Never drink coffee on an empty stomach.",
                "Latte art is 90% confidence, 10% milk foam.",
                "Life’s too short for bad coffee.",
                "Sip, don’t chug – coffee is a journey, not a race."
            ]
            print(random.choice(tips))

        elif choice == "credits":
            print('''Coffee Machine Program
Made with ☕ and ❤️ by S. Z. Mahdi.
Special thanks to caffeine for keeping this running!
            ''')

        elif choice == "cmds" or choice == "help":
            print('''Here is a list of all commands:

━━━━━━ GENERAL ━━━━━━
    espresso      - Order an espresso
    latte         - Order a latte
    cappuccino    - Order a cappuccino
    menu          - Show the drinks menu
    intro         - Displays the starting screen again
    report        - Show current resources and money
    status        - Alias for report
    history       - Show order history
    reset         - Reset resources and money
    joke          - Get a random programming joke
    tip           - Get a coffee tip
    time          - Show current time
    credits       - Show program credits
    cls           - Clear the screen
    off           - Turn off the coffee machine
    help/cmds     - Show this command list

━━━━━━ FUN ━━━━━━
    joke          - Get a random programming joke
    tip           - Get a coffee tip
    secret        - Discover a hidden easter egg

━━━━━━ ADMIN ━━━━━━
    admin         - Enter admin mode (password required)
     ↪  refill    - Refill resources to default
        srefill   - Super refill (1000 units each)
        report    - Show current resources and money
        exit      - Exit admin mode
            ''')

        elif choice == "intro":
            time.sleep(0.3)
            clear()
            intro()

        else:
            print("Invalid selection. Please choose espresso, latte, or cappuccino.")


if __name__ == "__main__":
    coffee_machine()


