# Simple function
# def greet():
#     print('hi')
#     print('hello')
#     print('olá')

# greet()

# Function with input:
# def greet_with_name(name):
#     print(f'hi {name}')
#     print(f'hello {name}')
#     print('olá')

# greet_with_name("John")

def greet_with(name,location):
    print(f'Hello, {name}')
    print(f'What is it like in {location}?')
# in this example: name and location are Position Parameters
greet_with("John", "Brasil")
# now, in this one, they are Keyword Arguments: 
greet_with(location='Brazil',name='John')