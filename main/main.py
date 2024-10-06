from main import randomizer
from random import randint
from main import cleaner
import csv

def air_ground_rb(country, localizator, user_limit, br, plane_choice):
    while True:
        vehicle = 'ground_planes'
        if user_limit > 0 and br > 0 and br <= 11 and user_limit <= 10:
            randomizer.main(user_limit, country, br, vehicle, plane_choice)
            break

def air_rb(country, localizator, user_limit):
    while True:
        try:
            br_mode = input(localizator['randomize'] + localizator['confirm']).lower()
            if br_mode == 'y' or br_mode == 'д':
                br = randint(1, 13)
                print(localizator['br'], br)
            elif br_mode == 'n' or br_mode == 'н':
                br = int(input(localizator['br_choice'] + ": '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13': "))
            vehicle = 'planes'
            if user_limit > 0 and br > 0 and br <= 13 and user_limit <= 10:
                randomizer.main(user_limit, country, br, vehicle, plane_choice = False)
                break
            else:
                print(localizator['rb_error'])
        except ValueError:
            print(localizator['rb_error'])

def ground_rb(country, localizator):
    while True:
        try:
            user_limit = int(input(localizator['user_limit']))
            br_mode = input(localizator['randomize'] + localizator['confirm']).lower()
            if br_mode == 'y' or br_mode == 'д':
                br = randint(1, 11)
            elif br_mode == 'n' or br_mode == 'н':
                br = int(input(localizator['br_choice'] + ": '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11': "))
            vehicle = 'tanks'
            plane_choice = input(localizator['plane_choice'] + localizator['confirm']).lower()
            if plane_choice == 'y' or plane_choice == 'д':
                plane_limit = int(input(localizator['plane_limit']))
                user_limit -= plane_limit
            if user_limit > 0 and br and br > 0 and br <= 11 and user_limit <= 10:
                print(localizator['br'], br)
                randomizer.main(user_limit, country, br, vehicle, plane_choice = False)
                if plane_choice == 'y' or plane_choice == 'д':
                    air_ground_rb(country, localizator, plane_limit, br, plane_choice)
                break
            elif plane_limit and user_limit <= 0:
                print(localizator['grb_plane_error'])
            else:
                print(localizator['rb_error'])
        except ValueError:
            print(localizator['rb_error'])
        except UnboundLocalError:
            print(localizator['rb_error'])

def csv_localisator(locale, localizator):
    for i in locale:
        for key, value in i.items():
            localizator[key] = value
    return localizator


while True:
    language = input('RU/EN: ').lower()

    if language.lower() == 'ru':
        break
    elif language.lower() == 'en':
        break
    else:
        print('Некорректный ввод/Incorrect input')

csv_locale = open(f'lang/{language}.csv', 'r', encoding='utf-8')
csv_reader = csv.DictReader(csv_locale, delimiter=';', fieldnames=['incorrect_enter','welcome', 'version', 'license', 'copyright', 'faction', 'grb', 'arb', 'mode_choice',
                                                                   'confirm', 'try_again', 'rb_error','user_limit', 'randomize','br_choice', 'plane_choice',
                                                                   'plane_limit', 'grb_plane_error', 'br'])
localizator = csv_localisator(csv_reader,localizator=dict())


print(localizator['welcome']+'\n'+localizator['version']+'\n'+localizator['license']+'\n'+localizator['copyright'])
while True:
    while True:
        country = input(localizator['faction']).upper()
        if country == 'US' or country == 'GE' or country == 'SU':
            break
        else:
            print(localizator['incorrect_enter'])
    cleaner.clear()
    print(localizator['grb']+'\n'+localizator['arb'])
    while True:
        mode_choise = input(localizator['mode_choice']).upper()
        if mode_choise == 'ТРБ' or mode_choise == 'GRB':
            ground_rb(country, localizator)
            break
        elif mode_choise == 'АРБ' or mode_choise == 'ARB':
            air_rb(country, localizator, user_limit=1)
            break
        else:
            print(localizator['incorrect_enter'])
    while True:
        while True:
            user_choice = input('\n'+localizator['try_again'] + localizator['confirm']).lower()
            if user_choice == 'y' or user_choice == 'n' or user_choice == 'д' or user_choice == 'н':
                break
            else:
                print(localizator['incorrect_enter'])
        if user_choice == 'y' or user_choice == 'д':
            cleaner.clear()
            if mode_choise == 'ТРБ' or mode_choise == 'GRB':
                ground_rb(country, localizator)
            elif mode_choise == 'АРБ' or mode_choise == 'ARB':
                air_rb(country, localizator, user_limit=1)
        elif user_choice == 'n' or user_choice == 'н':
            cleaner.clear()
            break
        else:
            print(localizator['incorrect_enter'])