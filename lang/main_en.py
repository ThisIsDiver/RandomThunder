from main import randomizer
from time import sleep
from random import randint
from main import cleaner

def air_rb(country, user_limit):
    while True:
        try:
            br_mode = input('Randomize BR? y/n: ').lower()
            if br_mode == 'y':
                br = randint(1, 13)
                print('BR:', br)
            elif br_mode == 'n':
                br = int(input("Enter BR in format: '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13': "))
            vehicle = 'planes'
            if user_limit > 0 and br > 0 and br <= 13 and user_limit <= 10:
                randomizer.main(user_limit, country, br, vehicle)
                break
            else:
                print('You did something wrong!')
        except ValueError:
            print('You did something wrong!')
def ground_rb(country):
    while True:
        try:
            user_limit = int(input('Enter the number of available crews or vehicle limit: '))
            br_mode = input('Randomize BR? y/n: ').lower()
            if br_mode == 'y':
                br = randint(1,11)
                print('BR:',br)
            elif br_mode == 'n':
                br = int(input("Enter BR in format: '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11': "))
            vehicle = 'tanks'
            if user_limit > 0 and br and br > 0 and br <= 11 and user_limit <= 10:
                randomizer.main(user_limit,country,br,vehicle)
                break
            else:
                print('You did something wrong!')
        except ValueError:
            print('You did something wrong!')
        except UnboundLocalError:
            print('You did something wrong!')

print('WELCOME!\nThis is RandomThunder - opensource software for random selection of vehicles\nVersion: 0.0.1 Reserve\nLicense: MIT\n©ThisIsDiver')
while True:
    while True:
        country = input('Enter faction: US, GE, SU - ').upper()
        if country == 'US' or country == 'GE' or country == 'SU':
            break
        else:
            print('ENTER FACTION CORRECTLY!')
    cleaner.clear()
    print(
        'Ground Realistic Battles - a mode of joint realistic battles, in which tanks, planes, helicopters fight on the same battlefield \n(currently only tanks are available, soon will be possible to choose with planes)\nAir Realistic Battles - a mode in which players of one team fight with another on planes')
    while True:
        mode_choise = input('GRB или ARB: ').upper()
        if mode_choise == 'GRB':
            ground_rb(country)
            break
        elif mode_choise == 'ARB':
            air_rb(country, user_limit = 1)
            break
        else:
            print('Enter CORRECTLY!')
    while True:
        user_choice = input('\nContinue? y/n: ').lower()
        if user_choice == 'y' or user_choice == 'n':
            break
        else:
            print('Please enter your answer correctly!')
    if user_choice == 'y':
        cleaner.clear()
    elif user_choice == 'n':
        print('Thank you for using the software!')
        sleep(3)
        break
    else:
        print('CRITICAL ERROR')
