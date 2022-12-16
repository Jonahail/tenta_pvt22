import requests


def get_winners(year, category):
    url = f"http://api.nobelprize.org/2.1/nobelPrizes?nobelPrizeYear={year}&nobelPrizeCategory={category}"
    response = requests.get(url)
    if response.status_code == 200:
        winners = []
        prizes = response.json()['nobelPrizes']
        for prize in prizes:
            for laureate in prize['laureates']:
                laureate_response = requests.get(laureate['links']['laureate'])
                if laureate_response.status_code == 200:
                    laureate = laureate_response.json()
                    laureate['prize_money'] = prize['prizeAmount']
                    laureate['category'] = prize['categoryFullName']['en']
                    winners.append(laureate)
        return winners
    else:
        return None

