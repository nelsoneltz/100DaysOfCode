# Greetings message;
print("Welcome to the tip calculator.")

# Input and cast for total bill as float
bill = float(input("What was the total bill? $"))

# Input and cast for percentage as int
percentage = int(input("What percentage tip would you like to give? 10,12, or 15? "))

# Input and cast for people as int
people = int(input("How many people to split the bill? "))

# Math applied usind PEMDAS
calc  = (bill/people) * (1 + percentage/100)

# Rounding float to 2 decimal places
calc = round(calc,2)

# Printing result
print(f'Each person should pay: ${calc}')