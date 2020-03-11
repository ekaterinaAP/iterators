import json

from countries.get_countries_list import get_countries_list
from countries.get_hash import get_hash
from countries.iterator_country import Country


def receive_country_url():
    countries_list = get_countries_list('countries.json')

    data = []

    for name_country in Country(countries_list):
        data.append(name_country)

    with open("about_countries.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    receive_country_url()

    for country in get_hash('about_countries.json'):
        print(country)

