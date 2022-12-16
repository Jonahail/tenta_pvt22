import requests

def nobel_data():
    results = requests.get("http://api.nobelprize.org/2.1/nobelPrizes")
    result_as_json = results.json()
    print(result_as_json)


def nobel_winners(nobel_data) -> str:
    winners = {}
    for winner in

print(nobel_data())