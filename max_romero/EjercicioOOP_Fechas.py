"""
Crea una clase Fecha. La clase contendrá además del constructor,
métodos set y get y el método __str__(), un método para comprobar
si la fecha es correcta y otro para modificar la fecha actual por otra.
"""

#Codigo realizado con getters y setters.

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def get_day(self):
        return self.day

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year

    def set_day(self, day):
        self.day = day

    def set_month(self, month):
        self.month = month

    def set_year(self, year):
        self.year = year

    def is_valid(self):
        return 0 < self.get_day() < 32 and 0 < self.get_month() < 13 and 1950 < self.get_year() < 2100

    def modify_date(self, day, month, year):
        self.set_day(day)
        self.set_month(month)
        self.set_year(year)

    def __str__(self):
        return f'{self.get_day()} / {self.get_month()} / {self.get_year()}'

date1 = Date(14,6,1991)

print(date1.get_day())
print(date1.get_month())
print(date1.get_year())
print(date1.is_valid())

date1.set_day(85)
date1.set_month(18)
date1.set_year(4510)

print(date1.is_valid())

#Codigo Realizado al estilo Python


""" class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def is_valid(self):
        return 0 < self.day < 32 and 0 < self.month < 13 and 1950 < self.year < 2100

    def modify_date(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'{self.day} / {self.month} / {self.year}'

date1 = Date(14,6,1991)

print(date1.day)
print(date1.month)
print(date1.year)
print(date1.is_valid)

date1.day = 85
date1.month = 25
date1.year = 4050

print(date1.is_valid())
"""