import requests
from bs4 import BeautifulSoup
lst_name = []
lst_money = []
lich = 1
while True:
    print(f'Page - {lich}')
    url = f'https://auto.ria.com/uk/legkovie/?page={lich}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    name = soup.find_all('span', class_='blue bold')
    money = soup.find_all('div', class_='price-ticket')
    print(url)

    for i, (x, y) in enumerate(zip(name, money)):
        print(x.text, y.text)
    lich = lich + 1
    if lich == 10:
        break

