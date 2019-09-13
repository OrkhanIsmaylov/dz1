k=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(k)): 
    k[i]=k[i]+1
    print(k[i])
stroka=str(input('Введите строку: '))
for j in stroka.split():
    print(j)

klas=[{'school_class:': '4a', 'score': [3,4,4,5,2]},{'school_class:': '5a', 'score': [4,4,4,5,5]},
        {'school_class:': '6a', 'score': [2,4,3,5,2]},]
s=0
n=0
for odin_class in klas:
            odin_class=sum(odin_class['score'])/len(odin_class['score'])
            s=odin_class+s
            n=n+1
            print(f'Средняя оценка для класса: {odin_class}')
school=s/n
print(f'Средняя оценка по школе: {school}')

    

