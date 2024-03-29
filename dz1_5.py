phone1 = {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'discount': 15}
phone2 = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 10}
phone3 = {'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10}
def discounted(price, discount, max_discount=20, name=""):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount or "iphone" in name.lower() or not name:
            return price
        else:
            return price - (price * discount / 100)
    except ValueError: 
        print('Непраильно заданы данные')
apple_deck = discounted('price',phone1['discount'],name=phone1["name"])
android_deck = discounted(phone2['price'],phone2['discount'],name=phone2["name"])
print(android_deck)
noname_deck = discounted(phone3['price'],phone3['discount'],name=phone3["name"])
print(noname_deck)