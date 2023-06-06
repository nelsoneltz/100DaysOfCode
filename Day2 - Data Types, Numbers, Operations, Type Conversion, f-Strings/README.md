## Project: Tip Calculator

### Objective: An app/script that calculate and split a bill among people, and also adding percentage tip on preset values.

### Concepts:

- Data Types:

```python
#String
string_type = "Hello"
also_string = "123"

#Integer
interger_type = 123

#Float
float_type = 123.45

#Boolean
bool_type = True # Or False
```

- Check Data Type using type()
- Use cast to force a type:

```python
variable = str(123) # will result in a string with text 123;
# or
variable_2 = int(170.95) # will result in 170 number, without 0.95;
```

- Mathematical Operators:

```python
3 + 5 # 8
7 - 4 # 3
3 * 2 # 6
6 / 3 # 2.0 <- it returns a float
2 ** 3 # 8
# Remember PEMDAS order of execution:
# Parentheses, Exponents, Multiplication, Division, Addition, Subtraction
# () then ** then * then / then + then -
```

- F-String:

```python
variable = 'Test'
print(f'This is a {variable}') # The result would be "This is a Test"
```

---

### Functions used:

- type() - Return type of variable
- round() - Rounds the number within the given number of decimals places.
- len() - Return the lenght of a string

---

Good Exercise:

- Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

```python
tdn = input("Type a two digit number: ") #tdn = two digit number
print(int(tdn[0])+int(tdn[1]))
```
