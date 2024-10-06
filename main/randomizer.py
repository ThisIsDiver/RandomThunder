from random import choice
from math import floor
def finder(dic,find):
    vehicles = []
    for i, n in dic.items():
        if floor(float(n)) == find:
            vehicles.append(i)
    return vehicles

def main(user_limit, country, find, vehicle, plane_choice):
    file = open(f'factions/{country}/{vehicle}.txt','r', encoding='utf-8')
    txt = file.read().split('\n')
    dic = dict()
    randomned = list()

    for i in txt:
        i = i.split(' - ')
        dic[i[0]] = i[1]
    file.close()
    vehicles = finder(dic,find)
    for i in range(len(vehicles)):
        if user_limit == i:
            break
        while True:
            rand = choice(vehicles)
            if rand not in randomned:
                randomned.append(rand)
                break
    if plane_choice == 'n' or plane_choice == 'n' or plane_choice == False:
        print('| ',end='')
    for i in randomned:
        print(i,end=' | ')