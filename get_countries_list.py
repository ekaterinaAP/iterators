import json


def get_countries_list(path):
    with open(path, encoding='utf8') as f:
        countries_file = json.load(f)
        countries_list = []
        for country in countries_file:
            countries_list.append(country["name"]["common"])
    return countries_list
