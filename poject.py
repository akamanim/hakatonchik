"""● марка (строка)
● модель (строка)
● год выпуска (целое число)
● объем двигателя (decimal, точность 1 знак)
● цвет (строка)
● тип кузова (поле одиночного выбора.
варианты: седан, универсал. купе, хэтчбек, минивен, внедорожник, пикап)
● пробег (целое число)
● цена (decimal, точность 2 знака)"""
import json
from bs4 import BeautifulSoup
import requests
import csv
base_dennih = 'bs.json'
base_csv = 'bs.csv'
def write_to_csv(data):
    with open(base_csv,'a') as file:
        write = csv.writer(file)
        write.writerow([data])

class GetMixin:
    def get_data(self):
        with open(base_dennih) as file:
            return json.load(file)
    def get_id(self):
        with open('id.txt', 'r') as file:
            id = int(file.read())
            id += 1
        with open('id.txt', 'w') as file:
            file.write(str(id))
        return id

class CreateMixin(GetMixin):
     def create(self):
        data = super().get_data()
        try:
            new_product = {
                'id' : super().get_id(),
                'mark' : input('Введите марку машины: '),
                'model' : input('Введите модель машины: '),
                'year ' :int(input("Введите год машины: ")),
                'engine' : round(float(input('Введите обьем двигателя: ')), 1),
                'color' :input('Введите цвет машины: '),
                'kuzov' : int(input('Введите тип кузова: (1-седан,2-универсал,3-купе,4-хэтчбек,5-минивен,6-внедорожник,7-пикап)')),
                'probeg' : int(input('Введите пробег: ')),
                'price' : round(int(input('Введите цену')),2),
            }   
        except:
            print('Не верный формат ввода данных!')
            CreateMixin().create()
        else:
            data.append(new_product)
            with open(base_dennih, 'w') as file:
                json.dump(data, file)
                print('succefully')
        a = input('Введите команду - (1-Create, 2-Listing, 3-Retrieve, 4-Update, 5-Delete) ')
        if a == '1':
            self.create()
        elif a == '2':
            Car().listing()
        elif a == '3':
            Car().retrieve()
        elif a == '4':
            Car().update()
        elif a == '5':
            Car().delete()
        else:
            print('Не вверная команда!')
class ListngMixin(GetMixin):
    def listing(self):
        print('Список машин: ')
        data = super().get_data()
        print (data)
        a = input('Введите команду - (1-Create, 2-Listing, 3-Retrieve, 4-Update, 5-Delete) ')
        if a == '1':
            self.create()
        elif a == '2':
            Car().listing()
        elif a == '3':
            Car().retrieve()
        elif a == '4':
            Car().update()
        elif a == '5':
            Car().delete()
        else:
            print('Не вверная команда!')
class RetriveMixin(GetMixin):
    def retrieve(self):
        data = super().get_data()
        try:
            id = int(input('Введите номер машины: '))
        except ValueError:
            print('Введите в числовом формате')
            self.retrieve()
        else:
            one_product = list(filter(lambda x: x['id'] == id, data))
            if not one_product:
                print('Машина не найдена')
            else:
                print(one_product[0])
                a = input('Введите команду - (1-Create, 2-Listing, 3-Retrieve, 4-Update, 5-Delete) ')
        if a == '1':
            self.create()
        elif a == '2':
            Car().listing()
        elif a == '3':
            Car().retrieve()
        elif a == '4':
            Car().update()
        elif a == '5':
            Car().delete()
        else:
            print('Не вверная команда!')

class UpdateMixin(GetMixin):
    def update(self):
        data = super().get_data()
        try:
            id = int(input('Введите номер машины: '))
        except ValueError:
            print('Введите в числовом формате')
            self.update()
        else:
            one_product = list(filter(lambda x: x['id'] == id, data))
            try:
                product = data.index(one_product[0])
            except:
                print('Такой машины нет!')
            else:
                boot = int(input('Какой пункт вы хотите исправить?(1-Марка,2-Модель,3-Год выпуска,4-Обьем двигателя,5-цвет,6-Кузов,7-Пробег,8-Цена):  '))
                try:
                    if boot == 1:
                        data[product]['mark'] = input('Введите новую марку: ')
                        print(data[product])
                    elif boot == 2:
                        data[product]['model'] = input('Введите новую модель: ')
                        print(data[product])
                    elif boot == 3:
                        data[product]['year'] = int(input('Введите новый год выпуска: '))
                        print(data[product])
                    elif boot == 4:
                        data[product]['engine'] = int(input('Введите новый обьем двигателя: '))
                        print(data[product])
                    elif boot == 5:
                        data[product]['color'] = input('Введите новый цвет: ')
                        print(data[product])
                    elif boot == 6:
                        data[product]['kuzov'] = input('Введите новый кузов: ')
                        print(data[product])
                    elif boot == 7:
                        data[product]['probeg'] = int(input('Введите новый пробег: '))
                        print(data[product])
                    elif boot == 8:
                        data[product]['price'] = int(input('Введите новую цену: '))
                        print(data[product])
                except:
                    print('Вы ввели  не верный формат')
                    self.update()
                else:
                    with open(base_dennih, 'w') as file:
                        json.dump(data, file)
                        a = input('Введите команду - (1-Create, 2-Listing, 3-Retrieve, 4-Update, 5-Delete) ')
        if a == '1':
            self.create()
        elif a == '2':
            Car().listing()
        elif a == '3':
            Car().retrieve()
        elif a == '4':
            Car().update()
        elif a == '5':
            Car().delete()
        else:
            print('Не вверная команда!')

class DeleteMixin(GetMixin):
    def delete(self):
        data = super().get_data()
        try:
            id = int(input('Введите номер машины: '))
        except:
            print('Вы ввели не в числовом формате!')
        else:
            one_product = list(filter(lambda x: x['id'] == id, data))
        if not one_product:
            print('Такой машины нет')
        product = data.index(one_product[0])
        data.pop(product)
        with open(base_dennih, 'w') as file:
            json.dump(data, file)
        a = input('Введите команду - (1-Create, 2-Listing, 3-Retrieve, 4-Update, 5-Delete) ')
        if a == '1':
            self.create()
        elif a == '2':
            Car().listing()
        elif a == '3':
            Car().retrieve()
        elif a == '4':
            Car().update()
        elif a == '5':
            Car().delete()
        else:
            print('Не вверная команда!')
class Car(CreateMixin,ListngMixin,RetriveMixin, UpdateMixin,DeleteMixin):
   def __init__(
         self,
         mark='',
         model='',
         year=0,
         engine=0,
         color='',
         kuzov='',
         probeg=0,
         price=0,
   ):

         self.mark = mark,
         self.model = model,
         self.year = year,
         self.engine = engine,
         self.color = color,
         self.kuzov = kuzov,
         self.probeg = probeg,
         self.price = price,

car = Car('Lexus','LX570', 2017,5.7,'White','Jeep',140000,20000)
# car.create()
# car.retrieve()
# car.update()
# car.delete()


def get_html(url):
    responce = requests.get(url)
    return responce.text 
def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    cars = soup.find('div',class_ = 'search-results-table').find_all('div', class_ = 'list-item list-label')

    # print(cars)

    for car in cars:
        mark = 'Porche'
        model = car.find('div',class_ = 'block title').find('h2',class_='name').text.strip().replace('Porsche', '')
        year = car.find('div', class_ = 'block info-wrapper item-info-wrapper').find('p', class_ ='year-miles').find('span').text.replace(' ', '')
        engine = ('Больше 3-х')
        color = 'Белый'
        kuzov = car.find('p',class_='body-type').text.strip()
        probeg = car.find('p',class_='volume').text.strip()
        price = car.find('div', class_='block price').find('strong').text.replace(' ','')
        # print(mark,model, year, engine,kuzov,probeg,price)
        new_product = {
                'id' : GetMixin().get_id(),
                'mark' : mark,
                'model' : model,
                'year ' :year,
                'engine' : engine,
                'color' :color,
                'kuzov' : kuzov,
                'probeg' :probeg,
                'price' : price,
            }   
        # print(new_product)
        write_to_csv(new_product)




        
    #     write_to_csv(data)
with open(base_csv, 'w') as file:
    write = file.write('Hello')
get_data(get_html('https://www.mashina.kg/search/porsche/all/?currency=2&sort_by=upped_at%20desc'))