
def p1():

    a = input()
    b = input()
    if a == b:
        print('Пароль принят')
    else:
        print('Пароль не принят')

def p2():

    n = int(input('Введите номер вашего места в плацкартном вагоне: '))
    print()
    if n > 36:
        print('Ваше место боковое')
    elif n % 2:
        print('Ваше место внизу')
    else:
        print('Ваше место наверху')

def p3():

    year = int(input())
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print('Год високосный')
    else:
        print('Этот год не високосный')

def p4():

    a = input('цвет1:')
    b = input('цвет2:')
    if a != 'красный' and a != 'желтый' and a != 'синий':
        print('ошибка цвета')
    elif b!='красный' and b!='желтый' and b!='синий':
        print('ошибка цвета')
    elif a == 'красный' and b == 'синий' or b == 'красный' and a == 'синий':
        print('фиолетовый')
    elif a == 'красный' and b == 'желтый' or b == 'красный' and a == 'желтый':
        print('оранжевый')
    elif a == 'синий' and b == 'желтый' or b == 'синий' and a == 'желтый':
        print('зеленый')
    elif a=='красный' and b=='красный':
        print('красный')
    elif a =='синий' and b =='синий':
        print('синий')
    elif a =='желтый' and b =='желтый':
        print('желтый')



p1(), p2(), p3(), p4()
