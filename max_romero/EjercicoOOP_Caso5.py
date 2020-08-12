"""
Crear una clase Tiempo, con atributos hora, minuto y segundo, que pueda ser instanciada indicando:
los tres atributos, sólo la hora y minuto,o sólo la hora. 
Crear además los métodos necesarios para modificar la hora en cualquier momento de forma manual.
Mantenga la integridad de los datos en todo momento definiendo de tipo “private”.
Crear  una  clase prueba_tiempo que prueba una hora concreta  
y la  modifique a su gusto mostrándola por pantalla."""

class Time:
    
    def __init__(self, hour,minutes='0',sec='0'):
        self.__hour=input('Ingrese la hora: ')
        self.__minutes=input('Ingrese los minutos: ')
        self.__sec=input('Ingrese los segundos: ')
    
    def set_hour(self, hour):
        self.__hour=hour
    
    def set_minutes(self, minutes):
        self.__minutes=minutes

    def set_sec(self, sec):
        self.__sec=sec

class Time_test(Time):
    pass
    #Aca agregar validacion de horario.
