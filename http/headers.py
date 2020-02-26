import requests

url = "https://icanhazdadjoke.com"

res = requests.get(url, headers={"Accept": "application/json"})

print(res.text)
print(res.json())