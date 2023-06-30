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
        if MENU[beverage]['ingredients']['water'] < resources['water'] and MENU[beverage]['ingredients']['coffee'] < resources['coffee'] and MENU[beverage]['ingredients']['milk'] < resources['milk']:
            return True
        else:
            return False
    else:
        if MENU[beverage]['ingredients']['water'] < resources['water'] and MENU[beverage]['ingredients']['coffee'] < resources['coffee']:
            return True
        else:
            return False



is_on = False

while not is_on:
    prompt = input("What would you like? (espresso/latte/capuccino): ")
    if prompt == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${resources["money"]}')
    elif prompt == 'off':
        is_on = True
    # elif prompt == 'test':
    #     print(process_coins(1,2,3,4))
    elif prompt == 'espresso':
        print(prompt)
        print(MENU[prompt]['cost'])
    elif prompt == 'latte':
        print(prompt)
        print(MENU[prompt]['cost'])
    elif prompt == 'capuccino':
        print(prompt)
        print(MENU[prompt]['cost'])
    else:
        continue
