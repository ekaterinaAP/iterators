import requests


class Country:

    def __init__(self, some_list):
        self.list = some_list
        self.session = requests.Session()
        self.start = 0
        self.end = len(self.list)

    def __iter__(self):
        return self

    def __next__(self):
        name_country = self.list[self.start]
        name_country1 = name_country.replace(' ', '_')
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        link = f'http://en.wikipedia.org/wiki/{name_country1}'

        try:
            resp = self.session.get(link)
            if resp.status_code == 200:
                return {name_country: link}
            else:
                return {name_country: 'Страница не найдена'}

        except requests.exceptions as err:
            print(err)