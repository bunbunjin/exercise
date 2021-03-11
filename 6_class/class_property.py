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


human_name = Human('bunbunjin')
print(type(human_name))

human_isinstance = isinstance(human_name, Human)
print(human_isinstance)

human_attribute = dir(human_name)
print(human_attribute)

human_man = human_name.man
print(human_man)

human_name.girl_ = input('You are name?')
name = human_name.output()
print(name)
