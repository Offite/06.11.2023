class Equipment:

    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year

    def action(self):
        return 'не определено'

    def __str__(self):
        return f'{self.name}, {self.make}, {self.year}'

    def __le__(self, other):
        if not isinstance(other, Equipment):
            raise TypeError
        return self.year <= other.year

class Printer(Equipment):

    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series

    def action(self):
        return 'печатает'

    def __str__(self):
        return f'{self.series} {self.name}, {self.make}, {self.year}'

class Scaner(Equipment):

    def  __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'сканирует в комп'

class Xerox(Equipment):

    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'копирует и печатает на листочек'

def allItems(sklad):
    for item in sklad:
        print(item)

def get_items(sklad, ename):
    for item in sklad:
        if isinstance(item, ename):
            print(item)

sklad = []
e = Equipment('Noname', 'X', 2000)
sklad.append(e)
s = Printer('H451','dsfsdf', 'asdasd', 1545)
sklad.append(s)
x = Xerox('sdfsdf', 'sdfsdf', 5000)
sklad.append(x)
e = Equipment('Noname', 'X', 2000)
sklad.append(e)
s = Printer('TH84','dsfsdf', 'asdasd', 1545)
sklad.append(s)
x = Xerox('sdfsdf', 'sdfsdf', 5000)
sklad.append(x)
# allItems(sklad)
qet_items(sklad, Equipment)