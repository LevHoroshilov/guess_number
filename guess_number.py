from random import randint
rand = randint(1,100)
while True:
    cobstv = int(input('Введите число '))
    if cobstv == rand:
        print('Yeah body,light weight baby')
        break
    elif cobstv < rand:
        print('Число меньше загаданного')
    else: print('Число больше загаданного')     