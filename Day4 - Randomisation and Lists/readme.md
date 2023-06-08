## Project: Rock Paper Scissor Game

### Objective: Create an app that imitates Rock Paper Scissors using random numbers.

### Concepts:

- Modules:
are libraries that have functions that you can use in your python code. You can even import module you created.

```python
import random

# NOW YOU CAN USE FUNCTIONS THAT ARE IN random

# If I have a python file in the same path as the original py script, you can import 
import my_file # you don't include .py extension

# NOW YOU USE FUNCTIONS THAT ARE IN my_file
```
- Random Library: is a library created by the developers of Python to create sudo-random numbers. Using the [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister) method.
    - To create random ints use randint(interval here);
    - To create random floats random()*max_value;
```python
import random

random_int = random.randint(0,10)
# randint includes both limits, 0 and 10 are included

random_float = random.random() * max_value
# if max_value = 3 -> random_float would be in range 0.000000 to 2.999999
```
- Lists: It is a more complex data structure. I can hold multiple types of data. They are created using the '[ ]' (square brackets sign).
    - Append Method - add value to end of the list;
    - Extend Method - add a list to the end of the list;
```python
fruits = ['Cherry','Apple','Banana']
fruits[0] # -> 'Cherry' is returned
fruits[0] = 'Pineapple' # changes the first value of the list
fruits # ['Pineapple','Apple','Banana']
```

