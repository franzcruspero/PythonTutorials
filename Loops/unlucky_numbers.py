numbers = range(1,21)

for x in numbers:
    if x == 4 or x == 13:
        print(f'{x}, x is unlucky')
    elif x % 2 == 0:
        print(f'{x}, x is even')
    else:
        print(f'{x}, x is odd')