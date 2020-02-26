import requests

url = "https://icanhazdadjoke.com/search"

res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": "cat"}
)


data = res.json()

print(data["results"])