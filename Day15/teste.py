from data import MENU,resources

def process_coins(quarters:int,dimes:int,nickles:int,pennies:int):
    total = 0.25*quarters +0.1*dimes + 0.05 *nickles + 0.01*pennies
    total = round(total,2)
    return total




is_on = False

while not is_on:
    prompt = input("What would you like? (espresso/latte/capuccino): ")
    if prompt == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
    elif prompt == 'off':
        is_on = True
    elif prompt == 'test':
        print(process_coins(1,2,3,4))