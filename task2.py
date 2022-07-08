from bs4 import BeautifulSoup
import requests


class Parser:
    def __init__(self):
        self.url = 'https://ru.wikipedia.org'
        self.result = {}
    
    def parse(self):
        new_url = '/w/index.php?title=Категория:Животные_по_алфавиту&subcatfrom=А&filefrom=А&pageuntil=Азиатский+муравей-портной#mw-pages'
        for _ in range(200):
            response = requests.get(f'{self.url}{new_url}')
            soup = BeautifulSoup(response.text, 'lxml')
            new_url = soup.find('div', {'id': 'mw-pages'}).find('a', text='Следующая страница')['href']
            for animal in soup.find('div', {'class': 'mw-content-ltr'}).find_all('li', {'class': ''}):
                if animal.text.startswith('A'):
                    return
                else:
                    if animal.text[0] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ':
                        yield animal.text[0]

    def run(self):
        print('подождите, идёт парсинг большого объёма данных...')
        for animal in self.parse():
            if animal in self.result:
                self.result[animal] += 1
            else:
                self.result[animal] = 1
        for letter in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ':
            print(f'{letter}: {self.result[letter]}')


if __name__ == '__main__':
    parser = Parser()
    parser.run()
