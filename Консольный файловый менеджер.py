

import os

import shutil
from shutil import copyfile, copytree

import sys

while True:
    print('1. СОЗДАТЬ ПАПКУ')
    print('2. УДАЛИТЬ ПАПКУ')
    print('3. КОПИРОВАТЬ ФАЙЛ')
    print('4. ПРОСМОТР СОДЕРЖИМОГО РАБОЧЕЙ ДИРЕКТОРИИ')
    print('5. ПОСМОТРЕТЬ ТОЛЬКО ПАПКИ')
    print('6. ПОСМОТРЕТЬ ТОЛЬКО ФАЙЛЫ')
    print('7. ПРОСМОТР ИНФОРМАЦИИ ОБ ОПЕРАЦИОННОЙ СИСТЕМЕ')
    print('8. СОЗДАТЕЛЬ ПРОГРАММЫ')
    print('9. ИГРАТЬ В ВИКТОРИНУ')
    print('10. МОЙ БАНКОВСКИЙ СЧЕТ')
    print('11. ВЫХОД')

    choice = input('Выбирите пункт меню: ')
    if choice == '1':
        create_file_folder = str(input('Введите название папки: '))
        os.mkdir(f' {create_file_folder}')
    elif choice == '2':
        delete_file_folder = str(input('Введите название папки, которую хотите удалить: '))
        os.rmdir(f' {delete_file_folder}')
    elif choice == '3':

        copy_file = str(input('Введите назваине файла, который хотите скопировать: '))
        new_copy_file = str(input('Введите новое название файла для копирования: '))
        copyfile(copy_file, new_copy_file)

    elif choice == '4':
        print(os.listdir())
    elif choice == '5':
        dirs = [d for d in os.listdir() if os.path.isdir(d)]
        print(dirs)
    elif choice == '6':
        files = [f for f in os.listdir() if os.path.isfile(f)]
        print(files)
    elif choice == '7':
        print(sys.platform)
    elif choice == '8':
        print('Создатель программы:', '\nКОРЫТКО ЮЛИЯ НИКОЛАЕВНА')
    elif choice == '9':
        def question_bornday(ask_bornday, date):
            bornday = input(ask_bornday)
            while bornday != date:
                print("Не верно")
                bornday = input(ask_bornday)


        question_bornday('Ввведите год рождения А.С.Пушкина:', '1799')
        question_bornday('Ввведите день рождения Пушкина в формате "день месяц"', '6 июня')  # Веести день рождения в формате день месяц

        print('Верно')
    elif choice == '10':
        invoice_amount = 0
        purchase_history = []

        while True:
            print('1. ПОПОЛНЕНИЕ СЧЕТА')
            print('2. ПОКУПКА')
            print('3. ИСТОРИЯ ПОКУПОК')
            print('4. ВЫХОД')

            choice = input('Выберите пункт меню: ')
            if choice == '1':
                refil = int(input("Пополните ваш счет, введя сумму: "))
                invoice_amount += refil
            elif choice == '2':
                refil = int(input("Введите сумму покупки: "))
                if refil > invoice_amount:
                    print("К сожалению, у вас недостаточно денег")
                else:
                    invoice_amount -= refil
                    purchase_name = str(input("Введите название покупки: "))
                    purchase_history.append((purchase_name, refil))

            elif choice == '3':
                print(purchase_history)
            elif choice == '4':
                break
            else:
                print('Неверный пункт меню')
    elif choice == '11':
        break
    else:
        print('Неверный пункт меню')










