import random
print('Welcome to the PyPassword Generator!')

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','?','#','$','%','&','(',')','*','+','=','-']

number_letters = int(input('How many letters would you like in your password? '))
number_numbers = int(input('How many numbers would you like in your password? '))
number_symbols = int(input('How many symbols would you like in your password? '))

lista = []

for char in range(1,number_letters+1):
    lista.append(random.choice(letters))
for char in range(1,number_numbers +1):
    lista.append(random.choice(numbers))
for char in range(1, number_symbols+1):
    lista.append(random.choice(symbols))

random.shuffle(lista)

password =''
for char in lista:
    password += char
print(password)
