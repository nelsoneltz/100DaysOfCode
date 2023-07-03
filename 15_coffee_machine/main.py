# Requirements
# 1 Print Report -- 
# 2 Check resources sufficient
# 3 Process coins
# 4 Check transaction successful
# 5 Make Coffee

from data import MENU,resources

def process_coins(quarters:int,dimes:int,nickles:int,pennies:int):
    total = 0.25*quarters +0.1*dimes + 0.05 *nickles + 0.01*pennies
    total = round(total,2)
    return total

def is_available(beverage):
    if 'milk' in MENU[beverage]['ingredients']:
        missing = []
        if MENU[beverage]['ingredients']['water'] > resources['water']:
            missing.append('water') 
        if MENU[beverage]['ingredients']['coffee'] > resources['coffee']:
            missing.append('coffee') 
        if MENU[beverage]['ingredients']['milk'] > resources['milk']:
            missing.append('milk') 

        if MENU[beverage]['ingredients']['water'] < resources['water'] and MENU[beverage]['ingredients']['coffee'] < resources['coffee'] and MENU[beverage]['ingredients']['milk'] < resources['milk']:
            return True,missing
        else:
            return False,missing
    else:
        missing = []
        if MENU[beverage]['ingredients']['water'] > resources['water']:
            missing.append('water') 
        if MENU[beverage]['ingredients']['coffee'] > resources['coffee']:
            missing.append('coffee') 

        if MENU[beverage]['ingredients']['water'] < resources['water'] and MENU[beverage]['ingredients']['coffee'] < resources['coffee']:
            return True,missing
        else:
            return False,missing

def machine_choice(prompt):
    boleano,lista = is_available(prompt)
    if not boleano:
        for item in lista:
            print(f'Sorry there is not enough {item}')
    else:
        print("Please insert coins.")
        quarter = int(input("How many quarters?: "))
        dime = int(input("How many dimes?: "))
        nickle = int(input("How many nickles?: "))
        penny = int(input("How many pennies?: "))
        money = process_coins(quarter,dime,nickle,penny)
        if money == MENU[prompt]['cost']:
            print("Here is your coffee!")
            resources['money'] += money
        elif money < MENU[prompt]['cost']:
            print("Sorry that's not enough money. Money refunded")
        elif money > MENU[prompt]['cost']:
            print(f"Here is your coffe, and also ${money-MENU[prompt]['cost']} for your change.")
            resources['money'] += money



# for value in MENU:
#     boleano,lista = is_available(value)
#     if not boleano:
#         for item in lista:
#             print(f'Sorry there is not enough {item}')



is_on = True

while not is_on:
    prompt = input("What would you like? (espresso/latte/capuccino): ")
    if prompt == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${resources["money"]}')
    elif prompt == 'off':
        is_on = False
    elif prompt == 'espresso':
        machine_choice(prompt)            
    elif prompt == 'latte':
        machine_choice(prompt)            
    elif prompt == 'capuccino':
        machine_choice(prompt)            
    else:
        continue
