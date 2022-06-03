import json
import requests
from bs4 import BeautifulSoup
from time import sleep
import random
from model import check_the_uniqueness_of_the_data

from collect_car_info import collect_car_info


def get_data(url):
    counter = 1
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,ru;q=0.8,ru-RU;q=0.7",
        "Cache-Control": "no-cache, private",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
    }

    cars_info = []

    while True:
        print(f'парсим страницу номер {counter}')
        r = requests.get(url=(url + str(counter)), headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        cars = soup.find_all('div', class_="listing-item__wrap")

        if not len(cars):
            print('Закончили')
            counter = 1
            break
        for item in cars:
            vin_label = item.find('div', class_='badge badge--vin')
            about = item.find('div', class_="listing-item__about")
            link = about.find('a', class_='listing-item__link')
            link_url = 'https://cars.av.by' + str(link.get('href'))
            id_car = link_url.split('/')[::-1][0]

            if check_the_uniqueness_of_the_data(id_car):
                sleep(random.randint(0, 1))
                if vin_label:
                    cars_info.append(collect_car_info(id_car, True))
                else:
                    cars_info.append(collect_car_info(id_car, False))
            else:
                continue
        counter += 1
        sleep(random.randint(0, 1))
    # with open('nissan.json', 'w') as file:
    #     json.dump(cars_info, file, indent=4, ensure_ascii=False)


def main():
    all_brands = [
        'https://cars.av.by/filter?brands[0][brand]=834&page=',  # Mitsubishi
        'https://cars.av.by/filter?brands[0][brand]=892&page=',  # Nissan
        'https://cars.av.by/filter?brands[0][brand]=1039&page=',  # Renault
        'https://cars.av.by/filter?brands[0][brand]=1279&page=',  # Lada
        'https://cars.av.by/filter?brands[0][brand]=1181&page=',  # Tayota
        'https://cars.av.by/filter?brands[0][brand]=1216&page=',  # Volkswagen
        'https://cars.av.by/filter?brands[0][brand]=683&page=',  # Mercedes-Benz
        'https://cars.av.by/filter?brands[0][brand]=1444&page=',  # Acura
        'https://cars.av.by/filter?brands[0][brand]=1&page=',  # Alfa Romeo
        'https://cars.av.by/filter?brands[0][brand]=6&page=',  # Audi
        'https://cars.av.by/filter?brands[0][brand]=8&page=',  # BMW
        'https://cars.av.by/filter?brands[0][brand]=1506&page=',  # Buick
        'https://cars.av.by/filter?brands[0][brand]=40&page=',  # Cadillac
        'https://cars.av.by/filter?brands[0][brand]=1998&page=',  # Chery
        'https://cars.av.by/filter?brands[0][brand]=41&page=',  # Chevrolet
        'https://cars.av.by/filter?brands[0][brand]=42&page=',  # Chrysler
        'https://cars.av.by/filter?brands[0][brand]=43&page=',  # Citroen
        'https://cars.av.by/filter?brands[0][brand]=1841&page=',  # Dacia
        'https://cars.av.by/filter?brands[0][brand]=46&page=',  # Daewoo
        'https://cars.av.by/filter?brands[0][brand]=47&page=',  # Daihatsu
        'https://cars.av.by/filter?brands[0][brand]=45&page=',  # Dodge
        'https://cars.av.by/filter?brands[0][brand]=301&page=',  # Fiat
        'https://cars.av.by/filter?brands[0][brand]=330&page=',  # Ford
        'https://cars.av.by/filter?brands[0][brand]=2012&page=',  # Geely
        'https://cars.av.by/filter?brands[0][brand]=372&page=',  # GMC
        'https://cars.av.by/filter?brands[0][brand]=1726&page=',  # Great Wall
        'https://cars.av.by/filter?brands[0][brand]=383&page=',  # Honda
        'https://cars.av.by/filter?brands[0][brand]=433&page=',  # Hyundai
        'https://cars.av.by/filter?brands[0][brand]=1343&page=',  # Infitini
        'https://cars.av.by/filter?brands[0][brand]=526&page=',  # Jaguar
        'https://cars.av.by/filter?brands[0][brand]=540&page=',  # Jeep
        'https://cars.av.by/filter?brands[0][brand]=545&page=',  # Kia
        'https://cars.av.by/filter?brands[0][brand]=572&page=',  # Lancia
        'https://cars.av.by/filter?brands[0][brand]=584&page=',  # Land Rover
        'https://cars.av.by/filter?brands[0][brand]=589&page=',  # LEXUS
        'https://cars.av.by/filter?brands[0][brand]=2586&page=',  # Lifan
        'https://cars.av.by/filter?brands[0][brand]=601&page=',  # Lincoln
        'https://cars.av.by/filter?brands[0][brand]=634&page=',  # Mazda
        'https://cars.av.by/filter?brands[0][brand]=1850&page=',  # Mini
        'https://cars.av.by/filter?brands[0][brand]=966&page=',  # Opel
        'https://cars.av.by/filter?brands[0][brand]=989&page=',  # Peugeot
        'https://cars.av.by/filter?brands[0][brand]=1238&page=',  # Volvo
        'https://cars.av.by/filter?brands[0][brand]=1310&page=',  # ГАЗ
        'https://cars.av.by/filter?brands[0][brand]=1551&page=',  # ЗАЗ
        'https://cars.av.by/filter?brands[0][brand]=2051&page=',  # Москвич
        'https://cars.av.by/filter?brands[0][brand]=1464&page=',  # УАЗ
        'https://cars.av.by/filter?brands[0][brand]=5019&page=',  # Эксклюзив
        'https://cars.av.by/filter?brands[0][brand]=1022&page=',  # Pontiac
        'https://cars.av.by/filter?brands[0][brand]=1485&page=',  # Porsche,
        'https://cars.av.by/filter?brands[0][brand]=1067&page=',  # Rover
        'https://cars.av.by/filter?brands[0][brand]=1085&page=',  # Saab
        'https://cars.av.by/filter?brands[0][brand]=1091&page=',  # SEAT
        'https://cars.av.by/filter?brands[0][brand]=1126&page=',  # Skoda
        'https://cars.av.by/filter?brands[0][brand]=2449&page=',  # Smart
        'https://cars.av.by/filter?brands[0][brand]=1597&page=',  # Ssang Yong
        'https://cars.av.by/filter?brands[0][brand]=1155&page=',  # Suzuki
        'https://cars.av.by/filter?brands[0][brand]=2521&page=',  # Tesla

    ]

    for page in all_brands:
        get_data(page)


if __name__ == '__main__':
    main()
