import os
import time
import random
import datetime
import pyjokes

# --- list of all commands ---
commands = {
    # Main commands
    'espresso': 'Order an espresso',
    'latte': 'Order a latte',
    'cappuccino': 'Order a cappuccino',
    'menu': 'Show the menu with prices',
    'report': 'Show resources report',
    'history': 'Show all orders made so far',
    'cmds': 'Show this command list',
    'off': 'Turn off the machine',

    # Fun commands
    'joke': 'Get a random programming joke',
    'tip': 'Get a random coffee/life tip',
    'time': 'Show the current time/date',
    'credits': 'Show program credits',
    'secret': 'Hidden easter egg (optional)',

    # Admin commands (for reference)
    'refill': 'Reset resources to normal',
    'srefill': 'Super refill (1000 each)',
    'report_admin': 'Show resources in admin mode',
    'exit': 'Exit admin mode'
}


# --- resources ---
water = 300
milk = 200
coffee = 100
money = 0.0

recipes = {
    'espresso': {'water': 50, 'milk': 0, 'coffee': 18, 'cost': 1.5},
    'latte': {'water': 200, 'milk': 150, 'coffee': 24, 'cost': 2.5},
    'cappuccino': {'water': 250, 'milk': 100, 'coffee': 24, 'cost': 3.0}
}

# --- helper functions ---
def report(water, milk, coffee, money):
    print(f'''
Resources:
  Water:  {water}ml
  Milk:   {milk}ml
  Coffee: {coffee}g
  Money:  ${money:.2f}
''')

def check_resources(choice, water, milk, coffee):
    rec = recipes.get(choice)
    if not rec:
        return "Invalid selection.", False
    missing = []
    if rec['water'] > water: missing.append('water')
    if rec['milk'] > milk: missing.append('milk')
    if rec['coffee'] > coffee: missing.append('coffee')
    if missing:
        return f"Sorry, not enough {', '.join(missing)}.", False
    return "Resources sufficient.", True

def process_coins(cost):
    print(f"Please insert coins. Cost: ${cost:.2f}")
    try:
        quarters = int(input("  How many quarters? "))   # $0.25
        dimes    = int(input("  How many dimes? "))      # $0.10
        nickels  = int(input("  How many nickels? "))    # $0.05
        pennies  = int(input("  How many pennies? "))    # $0.01
    except ValueError:
        print("Invalid input. Transaction cancelled.")
        return 0.0
    total = quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01
    return total

def make_coffee(choice):
    global water, milk, coffee, money
    rec = recipes[choice]
    water -= rec['water']
    milk  -= rec['milk']
    coffee -= rec['coffee']
    money += rec['cost']

    # record order history
    if not hasattr(coffee_machine, "orders"):
        coffee_machine.orders = []
    coffee_machine.orders.append(choice)

    print(f"✅ Here is your {choice}. Enjoy!")

# --- main loop ---
def coffee_machine():
    global water, milk, coffee, money

    # banner
    print("\n☕  Welcome to the Coffee Machine  ☕\n")

    if not hasattr(coffee_machine, "orders"):
        coffee_machine.orders = []

    while True:
        choice = input("\ncoffee-machine> ").lower().strip()

        if choice == "off":
            print("👋 Turning off. Goodbye!")
            break

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
                print(f"💰 Here is ${change:.2f} in change.")
            make_coffee(choice)

        elif choice == "report":
            report(water, milk, coffee, money)

        elif choice == "history":
            if not coffee_machine.orders:
                print("📜 No orders yet.")
            else:
                print("📜 Order history:")
                for idx, order in enumerate(coffee_machine.orders, 1):
                    print(f"  {idx}. {order.title()}")

        elif choice == "menu":
            print("Menu:")
            for drink, rec in recipes.items():
                print(f"  {drink.title():<10} ${rec['cost']:.2f}")

        elif choice == "joke":
            try:
                print(pyjokes.get_joke())
            except:
                jokes = [
                    "Why did the coffee file a police report? It got mugged!",
                    "Decaf? No thanks, I don’t like my coffee depresso."
                ]
                print(random.choice(jokes))

        elif choice == "time":
            print("⏰ Current time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        elif choice == "tip":
            tips = [
                "Pro tip: Never drink coffee on an empty stomach.",
                "Latte art is 90% confidence, 10% milk foam.",
                "Sip, don’t chug – coffee is a journey, not a race."
            ]
            print(random.choice(tips))

        elif choice == "credits":
            print("Coffee Machine Program — Made with ☕ and ❤️ by S. Z. Mahdi!")

        elif choice == "cmds":
            print("\n📋 Available commands:\n")
            for cmd, desc in commands.items():
                print(f"  {cmd:<12} - {desc}")
            print("\nType 'off' to exit the machine.")

        else:
            print("❌ Unknown command. Type 'cmds' for help.")

if __name__ == '__main__':
    coffee_machine()

