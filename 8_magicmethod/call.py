from bs4 import BeautifulSoup
import requests


class Adder:
    def __init__(self):
        self._values = []

    def add(self, x):
        self._values.append(x)

    def __call__(self):
        return sum(self._values)


class Printer:
    def __init__(self):
        self.string = None

    def printer_(self, strings):
        self.string = strings

    def __call__(self):
        return print(f'{self.string}')


class HTMLget:
    def __init__(self):
        self.text = None
        self.urls = None
        self.html = None

    def url(self, urls):
        res = requests.get(urls)
        self.html = BeautifulSoup(res.text, 'html.parser')

    def __call__(self):
        return print(f'{self.html}')


adder = Adder()
adder.add(9)
adder.add(1)
print(adder())

printer = Printer()
printer.printer_('Hello!!')
printer()

printer.printer_('a')
printer()

task = HTMLget()
task.url('https://www.google.com/search?q=news&sxsrf=ALeKk01z6acr_4ldL9E0Qt6MuZ1-8qWHkw:1621072238483&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjN7bfXtMvwAhUBZt4KHSoUAjIQ_AUoAXoECAEQAw&biw=1420&bih=764')
task()
