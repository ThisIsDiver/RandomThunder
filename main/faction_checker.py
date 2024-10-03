from os.path import join, abspath, isdir
from os import listdir
from math import floor
from time import sleep
from os import getppid, kill
import signal

def checker(path):
    for file in listdir(path):
        if file == '__pycache__':
            b_red = True
        elif isdir(join(path,file)):
            checker(join(path,file))
        else:
            print(join(path,file))
            txt = open(join(path,file),'r', encoding='utf-8').read().split('\n')
            dic = dict()
            for i in txt:
                i = i.split(' - ')
                dic[i[0]] = i[1]
            for name, br in dic.items():
                try:
                    br_correct_check = floor(float(br))
                    print(name,'-', br)
                except:
                    print(f'Проверьте правильность файла/Check if the file is correct:\n{join(path,file)})')
                    sleep(10)
                    exit()

            print('------------------------------------------------------------')



factions_path = abspath(join('factions'))
print('------------------------------------------------------------')
checker(factions_path)
