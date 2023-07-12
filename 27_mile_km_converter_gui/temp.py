def add(*args):
    return sum(args)

print(add(3,5,3))

def calculate(**kwargs):
    pass

calculate(add=3,multiply=5)