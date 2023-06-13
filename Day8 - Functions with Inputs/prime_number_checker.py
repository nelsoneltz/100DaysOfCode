import random


def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Prime Number")
    else: 
        print("Not prime number")


num = int(input("Type a number "))
prime_checker(num)