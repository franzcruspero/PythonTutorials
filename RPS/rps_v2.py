from random import choice

p2 = choice(['rock', 'paper', 'scissors'])

print('...rock...')
print('...paper...')
print('...scissors...')

p1 = input('Enter your choice: ').casefold()

print(f'The computer plays {p2}')
if p1 == p2:
    print('It\'s a draw!')
elif p1 == 'rock':
    if p2 == 'scissors':
        print('Player 1 wins!')
    else:
        print('Player 2 wins!')
elif p1 == 'paper':
    if p2 == 'rock':
        print('Player 1 wins!')
    else:
        print('Player 2 wins!')
elif p1 == 'scissors':
    if p2 == 'paper':
        print('Player 1 wins!')
    else:
        print('Player 2 wins!') 
else:
    print('Invalid choice!')