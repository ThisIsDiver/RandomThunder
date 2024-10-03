from time import sleep

while True:
    language = input('RU/EN: ')

    if language.lower() == 'ru':
        from lang import main_ru
        break
    elif language.lower() == 'en':
        from lang import main_en
        break
    else:
        print('Некорректный ввод/Incorrect input')