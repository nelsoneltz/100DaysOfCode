
### SCOPE ###
# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# LOCAL SCOPE

# def drink_potion():
#     potion_strenght = 2
#     print(potion_strenght)

# drink_potion()
# print(potion_strenght) # THIS WILL GIVE AN ERROR 

# GLOBAL SCOPE

# player_health = 10

# def drink_potion():
#     potion_strenght = 2
#     print(player_health)

# drink_potion()
# print(player_health)


# THERE IS NO BLOCK SCOPE IN PYTHON

# game_level = 3

# def create_enemy():
#     enemies = ['Skeleton','Zombie','Alien']
#     if game_level <5:
#         new_enemy = enemies[0]
# print(new_enemy) # ALSO AN ERROR 


# MODIFYING GLOBAL SCOPE

# enemies = 1

# def increase_enemies():
#     return enemies + 1


# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

# GLOBAL CONSTANTS
# best practice to set a global variable as all UPPER case
PI = 3.14159
URL = 'www.google.com'

