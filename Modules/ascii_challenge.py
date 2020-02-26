from termcolor import colored
from pyfiglet import figlet_format

valid_colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')

message = input('What message do you want to print? ')
color = input('In what color? ')

if color not in valid_colors:
    color = 'blue'

figlet_message = figlet_format(message)
print(colored(figlet_message, color))


