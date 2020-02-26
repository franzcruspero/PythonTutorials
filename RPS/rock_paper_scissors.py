print('Time to play Rock Papers Scissors!')
player1 = input('enter player 1\'s choice: ')
print('**NO CHEATING**\n\n' * 20)
player2 = input('enter player 2\'s choice: ')


if player1 and player2:
    if player2 == 'rock' or player2 == 'scissors' or player2 == 'paper':
        if player1 == player2:
            print('It\'s a draw!')
        elif player1 == 'rock':
            if player2 == 'scissors':
                print('Player 1 wins!')
            elif player2 == 'paper':
                print('Player 2 wins!')
        elif player1 == 'paper':
            if player2 == 'rock':
                print('Player 1 wins!')
            elif player2 == 'scissors':
                print('Player 2 wins!')
        elif player1 == 'scissors':
            if player2 == 'paper':
                print('Player 1 wins!')
            elif player2 == 'rock':
                print('Player 2 wins!')
        else:
            print('Something went wrong!')
    else:
        print('Something went wrong!')
else:
    print('You need an input from both players!')
    
        
    
