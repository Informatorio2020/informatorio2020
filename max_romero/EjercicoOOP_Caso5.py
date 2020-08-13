"""
Crear una clase Tiempo, con atributos hora, minuto y segundo, que pueda ser instanciada indicando:

los tres atributos, sólo la hora y minuto,o sólo la hora.[]
Crear además los métodos necesarios para modificar la hora en cualquier momento de forma manual.[]
Mantenga la integridad de los datos en todo momento definiendo de tipo “private”.[]

Crear  una  clase prueba_tiempo que prueba una hora concreta[]  
y la  modifique a su gusto mostrándola por pantalla.[]
"""

class Time:
    
    def __init__(self, hour,minutes='0',sec='0'):
        self.__hour=hour
        self.__minutes=minutes
        self.__sec=sec


#Get hora completa 
    
    def get_time(self):
        return f'{self.__hour} Horas, {self.__minutes} Minutos y {self.__sec} segundos'

#Set att

    def set_hour(self, hour):
        self.__hour=hour
    
    def set_minutes(self, minutes):
        self.__minutes=minutes

    def set_sec(self, sec):
        self.__sec=sec

#Get att

    def get_hour(self):
        return {self.__hour}

    def get_minutes(self):
        return {self.__minutes}

    def get_sec(self):
        return {self.__sec}
    
"""Validacion 

    def is_valid(self):
        return 0 > self.get_hour() < 25 and 0 > self.get_minutes() < 61 and 0 > self.get_sec() < 61 
"""

class Time_test(Time):
    pass

hour=int(input('Ingrese la hora: '))
minutes=int(input('Ingrese los minutos: '))
sec=int(input('Ingrese los segundos '))

time_is = Time(hour,minutes=0,sec=0)

