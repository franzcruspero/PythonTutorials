from random import randint

random_number = randint(1,10)

answer = input('Pick a number between 1 and 10: ')

while True:
    answer = int(answer)
    if answer == random_number:
        print('You guessed it! You won!')
        flag = input('Do you want to keep playing? (y/n): ')
        if flag == "y":
            random_number = randint(1,10)
            answer = input('Pick a number between 1 and 10: ')
        elif flag == "n":
            break
        else:
            print('It\'s a yes or no question!')
    elif answer < random_number:
        print('Too low, try again!')
        answer = input('Pick a number between 1 and 10: ')
    else:
        print('Too high, try again!')
        answer = input('Pick a number between 1 and 10: ')