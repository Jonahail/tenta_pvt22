import requests

help_string = """
Ange ett år och fält
Exempelvis 1965 fysik

Fält att välja från:
fysik, kemi, litteratur, ekonomi, fred, medicin

Om du vill avsluta programmet -> tryck Q
För att se hjälptext -> tryck H
"""
print(help_string)

categori = {"fysik": "phy",
       "kemi": "che",
       "litteratur": "lit",
       "ekonomi": "eco",
       "fred": "pea",
       "medicin": "med"}


def main():
    while True:

        aaa = input(">")
        if aaa.lower() == "q":
            break
        elif aaa.lower() == "h":
            print(help_string)
            continue

        try:
            year, field = aaa.split()
            year = int(year)
            c = categori[field]
        except ValueError:
            print("Ange ett år och fält")
            continue
        except KeyError:
            print("Ange ett år och fält")
            continue

        params = {"nobelPrizeYear": year, "nobelPrizeCategory": c}

        res = requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=params).json()


        for person in res["nobelPrizes"]:
            peng = person["prizeAmount"]
            idagpeng = person["prizeAmountAdjusted"]
            print(f"{person['categoryFullName']['se']} prissumma {peng} SEK")

            for m in person["laureates"]:
                print("---------")
                print(m['knownName']['en'])
                print(m['motivation']['en'])
                andel = m['portion']


if __name__ == '__main__':
    main()
