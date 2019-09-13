question_ask={"Как дела": "Хорошо", "Что делаешь?": "Программирую"}

d=str(input('Как дела?: '))
def ask_user(d):
    try:
        while True:
                if d=='Хорошо':
                    break
                elif d in question_ask.keys():
                    print(question_ask[d])
                    break
                else:
                    d=str(input('Как дела?: '))    
    except KeyboardInterrupt:
        print('Пока') 
ask_user(d)




    