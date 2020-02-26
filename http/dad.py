import requests
from termcolor import colored
from pyfiglet import figlet_format
from random import choice

def welcome_message():
    message = figlet_format("Dad Joke 3000")
    print(colored(message, "blue"))

def make_request(topic):
    url = "https://icanhazdadjoke.com/search"
    res = requests.get(
        url,
        headers = {"Accept": "application/json"},
        params = {"term": topic}
    )
    data = res.json()
    response_length = data['total_jokes']
    results = data["results"]

    if response_length > 1:
        print(f"I've got {response_length} jokes about {topic}. Here's one:")
        return choice(results)['joke']
    elif response_length == 1:
        print(f"I've got {response_length} joke about {topic}. Here it is:")
        return results[0]['joke']
    else:
        return (f'Sorry, I don\'t have any jokes about {topic}! Please try again')


welcome_message()
topic = input("Let me tell you a joke! Give me a topic: ")
res = make_request(topic)
print(res)

