from operator import attrgetter


class Human:
    def __init__(self, man):
        if man != 'bunbunjin':
            raise ValueError('Who are you!!')
        self.man = man
        self.girl = None

    @property
    def girl_(self):
        return self.girl

    @girl_.setter
    def girl_(self, girl):
        if girl == 'bunbunjin':
            raise ValueError("I'm bunbunjin")
        self.girl = girl
        return self.girl

    def output(self):
        return f'{self.man}と{self.girl}'


class Drink:
    def __init__(self, kind, num):
        self.kind = kind
        self.num = num
        self._price = 0
        self._discount = 0

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, _discount):
        if _discount < 0 or 1000 < _discount:
            raise ValueError('')
        self._discount = _discount
        return self._discount

    @property
    def price(self, _price):
        return self._price

    @price.setter
    def price(self, _price):
        if _price < 0:
            raise ValueError('miss input')
        self._price = _price
        return self._price

    def output(self):
        discount_price = self._price - self._discount
        return f'種類:{self.kind}\n個数:{self.num}\n価格:{discount_price}'


human_name = Human('bunbunjin')
print(type(human_name))

human_isinstance = isinstance(human_name, Human)
print(human_isinstance)

human_attribute = dir(human_name)
print(human_attribute)

human_man = human_name.man
print(human_man)

human_name.girl_ = 'bunbunko'
name = human_name.output()
print(name)

drink_order = Drink('Coffee', 1)
drink_order.price = 500
drink_order.discount = 100
drink_output = drink_order.output()
print(drink_output)
