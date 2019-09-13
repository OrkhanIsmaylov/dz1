stroka1='Привет, я делаю дз'
stroka2='Пока я все сделал'
def proverka(stroka1,stroka2):
    if stroka1!=str(stroka1) or stroka2!=str(stroka2):
        return 0
    elif stroka1==stroka2:
        return '1'
    elif stroka1!=stroka2 and len(stroka1)==len(stroka2):
        return '2'
    elif stroka1!=stroka2 and stroka2=='learn':
        return '3'
    else:
        return 'нет условия'
print(proverka(stroka1,stroka2))

