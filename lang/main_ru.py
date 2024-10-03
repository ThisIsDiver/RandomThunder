from main import randomizer
from time import sleep
from random import randint
from main import cleaner

def air_rb(country, user_limit):
    while True:
        try:
            br_mode = input('Рандомный БР? y/n: ').lower()
            if br_mode == 'y':
                br = randint(1, 13)
                print('БР:', br)
            elif br_mode == 'n':
                br = int(input("Введите БР в формате: '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13': "))
            vehicle = 'planes'
            if user_limit > 0 and br > 0 and br <= 13 and user_limit <= 10:
                randomizer.main(user_limit, country, br, vehicle)
                break
            else:
                print('Вы что-то сделали не так!')
        except ValueError:
            print('Вы что-то сделали не так!')
def ground_rb(country):
    while True:
        try:
            user_limit = int(input('Введите количество доступных экипажей или лимит техники: '))
            br_mode = input('Рандомный БР? y/n: ').lower()
            if br_mode == 'y':
                br = randint(1,11)
                print('БР:',br)
            elif br_mode == 'n':
                br = int(input("Введите БР в формате: '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11': "))
            vehicle = 'tanks'
            if user_limit > 0 and br and br > 0 and br <= 11 and user_limit <= 10:
                randomizer.main(user_limit,country,br,vehicle)
                break
            else:
                print('Вы что-то сделали не так!')
        except ValueError:
            print('Вы что-то сделали не так!')
        except UnboundLocalError:
            print('Вы что-то сделали не так!')

print('ПРИВЕТСТВУЮ!\nЭто RandomThunder - программное обеспечение с открытым исходным кодом для случайного подбора техники\nВерсия: 0.0.1 Reserve\nЛицензия: MIT\n©ThisIsDiver')
while True:
    while True:
        country = input('Введите фракцию: US, GE, SU - ').upper()
        if country == 'US' or country == 'GE' or country == 'SU':
            break
        else:
            print('ВВЕДИТЕ ФРАКЦИЮ КОРРЕКТНО!')
    cleaner.clear()
    print(
        'Танковые реалистичные бои - режим совместных реалистичных боёв, в рамках которых танки, самолёты, вертолёты сражаются на одном поле битвы \n(пока что доступен выбор только танков, скоро возможность выбрать с самолётами)\nАвиационные реалистичные бои - режим, в рамках которого игроки одной команды сражаются с другой на самолётах')
    while True:
        mode_choise = input('ТРБ или АРБ: ').upper()
        if mode_choise == 'ТРБ':
            ground_rb(country)
            break
        elif mode_choise == 'АРБ':
            air_rb(country, user_limit = 1)
            break
        else:
            print('Введите ПРАВИЛЬНО!')
    while True:
        user_choice = input('\nПродолжить? y/n: ').lower()
        if user_choice == 'y' or user_choice == 'n':
            break
        else:
            print('Введите ответ корректно!')
    if user_choice == 'y':
        cleaner.clear()
    elif user_choice == 'n':
        print('Спасибо за использование программы!')
        sleep(3)
        break
    else:
        print('CRITICAL ERROR')
