def proverka(stroka1,stroka2):
    if not isinstance(stroka1,str) or not isinstance(stroka2,str):
        return '0'
    elif stroka1 == stroka2:
        return '1'
    elif stroka1 != stroka2 and len(stroka1) == len(stroka2):
        return '2'
    elif stroka1 != stroka2 and stroka2 == 'learn':
        return '3'
    else:
        return 'нет условия'

stroka1 = 'Привет, я делаю дз'
stroka2 = 'Пока, я все сделал'

if __name__ == "__main__":
    print(proverka(stroka1,stroka2))

