# Write a program that simulates the children FizzBuzz game.
# From 1 to 100:
# If a number is divisible by 3 -> Fizz
# If a number is divisible by 5 -> Buzz
# If a number is divisible by both 3 and 5 -> FizzBuzz

lista = []
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0 :
        lista.append('FizzBuzz')
    elif number % 3 == 0:
        lista.append('Fizz')
    elif number % 5 == 0:
        lista.append('Buzz')
    else:
        lista.append(number)
print(lista)