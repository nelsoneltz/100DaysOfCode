## Project: Treasure Island Game

### Objective: Create a game of choices using Conditional and Logical statements.

### Concepts:

- If/Else:

```python
#Structure
    if condition:
        do this
    else:
        do this
```

- Nested If/Else:

```python
#Structure
    if condition:
        if another condition:
            do this
        else:
            do this
    else:
        do this
```

- Elif:

```python
#Structure
    if condition:
        do this
    elif:
        do this
    else:
        do this
```

- Multiple If:

```python
#Structure
    if condition:
        do this
    if condition:
        do this
    if condition:
        do this
```

- Modulo Math Operator:

```python
#Structure
 7 % 2 # 1
```

Good Exercise:

- Write an script that calculates the BMI given Height (m) and Weight (kg) and give a response. Round the BMI to whole number.

```python
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
math  =  round(weight / (height * height),0)
print(math)

if math < 18.5:
    print(f'Your BMI is {int(math)}, you are underweight.')
elif math < 25:
    print(f'Your BMI is {int(math)}, you have a normal weight.')
elif math < 30:
    print(f'Your BMI is {int(math)}, you are slightly overweight.')
elif math < 35:
    print(f'Your BMI is {int(math)}, you are obese.')
else:
    print(f'Your BMI is {int(math)}, you are clinically obese.')

```
