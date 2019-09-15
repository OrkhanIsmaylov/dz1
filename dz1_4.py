def ask_user(d):
    try:
        while True:
            d=str(input('Как дела?: '))
                if d=='Хорошо':
                    break
                elif d in question_ask:
                    print(question_ask[d])
                    break    
    except KeyboardInterrupt:
        print('Пока') 

question_ask={"Как дела": "Хорошо", "Что делаешь?": "Программирую"}

d=str(input('Как дела?: '))

if __name__ == "__main__":
    ask_user(d)




    