from random import choice
from math import floor
def finder(dic,find):
    vehicles = []
    for i, n in dic.items():
        if floor(float(n)) == find:
            vehicles.append(i)
    return vehicles

def main(user_limit, country, find, vehicle):
    txt = open(f'factions/{country}/{vehicle}.txt','r', encoding='utf-8').read().split('\n')
    dic = dict()
    randomned = list()

    for i in txt:
        i = i.split(' - ')
        dic[i[0]] = i[1]
    vehicles = finder(dic,find)
    for i in range(len(vehicles)):
        if user_limit == i:
            break
        while True:
            rand = choice(vehicles)
            if rand not in randomned:
                randomned.append(rand)
                break
    print('| ',end='')
    for i in randomned:
        print(i,end=' | ')
