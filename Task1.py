# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

def checknumber(num):
    if num == 6 or num == 7:
        print('Это выходной день')
    elif 1 <= num <= 5:
        print('Это рабочий день')
    else:
        print('Это не день недели. Введите порядковый номер дня недели от 1 до 7')


DayNumber = int(input('Введите порядковый номер дня недели от 1 до 7: '))
checknumber(DayNumber)
