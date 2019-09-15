#задание1
def age(vozrast):
    if 0 <= vozrast <= 5:
        return 'Вы ходите в садик'
    elif 6 <= vozrast <= 18:
        return 'Вы ходите в школу'
    elif 19 <= vozrast <=25:
        return 'Вы учитесь в вузе'
    elif vozrast > 25:
        return 'Вы работаете'
    else:
        return 'Вы ввели неправильный возраст'

vozrast = int(input('Введите возраст: '))

if __name__ == "__main__":
    print(age(vozrast))
